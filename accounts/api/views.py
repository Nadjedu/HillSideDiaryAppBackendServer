import logging

from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import transaction
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import UserCreateSerializer, UserRetrieveSerializer, UserUpdateSerializer
from ..models import User
from .permissions import CanActionUser

logger = logging.getLogger(__name__)


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    lookup_field = "user_uuid"
    queryset = User.objects.all()

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        """
        Extends the create process to allow token generation when
        a user is created.
        :return Response object with a token field in headers containing
        access token and refresh token.
        """
        response = super(UserViewSet, self).create(request, *args, **kwargs)

        if response.status_code == 201:  # user row was created. Generate user token
            user_uuid = response.data["user_uuid"]
            user = User.objects.get(user_uuid=user_uuid)
            refresh = RefreshToken.for_user(user)
            response["token"] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }

        return response

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "me":
            return UserRetrieveSerializer
        if self.action == "update" or self.action == "partial_update":
            return UserUpdateSerializer

        return UserCreateSerializer

    def get_permissions(self):
        permissions = []

        if self.action == "retrieve" or self.action == "update":
            permissions = [IsAuthenticated, CanActionUser]
        if self.action == "create":
            permissions = [AllowAny]
        if self.action == "me":
            permissions = [IsAuthenticated]

        return [permission() for permission in permissions]

    @action(methods=['get'], detail=False)
    def me(self, request):
        return Response(self.get_serializer(self.request.user).data, status=status.HTTP_200_OK)
