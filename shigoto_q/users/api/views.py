from __future__ import absolute_import

from django.contrib.auth import get_user_model
from django.http import Http404
from djstripe.models import Product
from rest_framework.response import Response
from rest_framework.views import APIView

from rest.views import ResourceListView, ResourceView
from shigoto_q.users.api.serializers import (
    ProductSerializer,
    UserDumpSerializer,
    UserListSerializer,
    UserLoadSerializer,
)
from shigoto_q.users.services import users as user_services

User = get_user_model()


class UsersListView(ResourceListView):
    serializer_dump_class = UserListSerializer
    serializer_load_class = UserListSerializer

    def fetch(self, filters):
        return user_services.list_users(filters=filters)


class UserView(ResourceView):
    serializer_dump_class = UserDumpSerializer
    serializer_load_class = UserLoadSerializer
    request_param = "user"
    owner_check = True

    def fetch_one(self, pk):
        if pk == "me":
            pk = self.request.user.id
        return user_services.get_user(pk=pk)


class UserCreateView(ResourceView):
    serializer_dump_class = UserDumpSerializer
    serializer_load_class = UserLoadSerializer
    http_method_names = ["post"]
    permission_classes = []

    def execute(self, data):
        return user_services.create_user(data=data)


class ProductView(APIView):
    permission_classes = []

    def get_objects(self, *args, **kwargs):
        try:
            return (
                Product.objects.prefetch_related("plan_set")
                .order_by("plan__amount")
                .filter(plan__interval="month")
            )
        except Product.DoesNotExist:
            return Http404

    def get(self, request, *args, **kwargs):
        products = self.get_objects()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
