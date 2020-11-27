from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import get_user_model as User
from rest_framework import status, views, generics, authentication, permissions
from rest_framework.response import Response
from .serializers import UserSerializer, SignUpSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class UserView(generics.ListCreateAPIView):
    # authentication_classes = [authentication.TokenAuthentication, authentication.BasicAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User().objects.all()
    serializer_class = UserSerializer


class SingleUserView(generics.RetrieveAPIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User().objects.all()
    serializer_class = UserSerializer


class SignUp(views.APIView):
    def get_object(self, email):
        try:
            return User().objects.get(email=email)
        except User().DoesNotExist:
            return None

    def sign_up_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = self.get_object(email)
            if user is None:
                serializer.save()
                user = self.get_object(email)
                data = self.sign_up_token(user)
                data[id] = user.id
                return Response({"Response": data}, status=status.HTTP_200_OK)
            return Response("Invalid Username or Password")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Logout(views.APIView):

    def post(self, request, *args, **kwargs):
        access_token = request.data.get("access")
        success_token = request.data.get("refresh")