from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.views import APIView
from django.contrib.auth import get_user_model, login, logout
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .serializers import (
    UserCreateSerializer,
    UserModificationSerializer,
    UserLoginSerializer,
    UserPasswordChangeSerializer,
    UserDetailSerializer,
)
from .permissions import IsOwnerOrReadOnly

User = get_user_model()


class DetailUserAPIView(RetrieveAPIView):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    class Meta:
        model = User


class CreateUserAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny, ]

    class Meta:
        model = User


class ModifyUserAPIView(UpdateAPIView):
    serializer_class = UserModificationSerializer
    lookup_field = 'username'
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = (TokenAuthentication, SessionAuthentication,)

    class Meta:
        model = User


class LoginUserAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (TokenAuthentication, SessionAuthentication, )
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=HTTP_200_OK)

    class Meta:
        model = User


class LogoutUserAPIView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = (TokenAuthentication, SessionAuthentication, )

    def get(self, request):
        token = Token.objects.get(user=request.user)
        token.delete()
        logout(request)
        return Response(status=HTTP_204_NO_CONTENT)

    class Meta:
        model = User


class ChangePasswordAPIView(APIView):
    serializer_class = UserPasswordChangeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = (TokenAuthentication, SessionAuthentication,)

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = UserPasswordChangeSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]},
                                status=HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("password"))
            self.object.save()
            return Response(status=HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    class Meta:
        model = User
