from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import get_user_model as User
from rest_framework import status, views, generics, authentication, permissions, decorators, viewsets, exceptions
from rest_framework.response import Response
from .serializers import UserSerializer, ExamSerializer, QuestionSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt import authentication as jwt_auth
# from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from .models import Exam, Question
from .permissions import IsExamAuthor, IsQuestionAuthor


class UserView(generics.ListCreateAPIView):
    authentication_classes = [jwt_auth.JWTAuthentication]
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = User().objects.all()
    serializer_class = UserSerializer

class SingleUserView(generics.RetrieveAPIView):
    authentication_classes = [jwt_auth.JWTAuthentication]
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = User().objects.all()
    serializer_class = UserSerializer

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def SignUp(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        data[id] = user.id
        return Response(data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Logout(views.APIView):
# work in progress
    def post(self, request, *args, **kwargs):
        access_token = request.data.get("access")
        success_token = request.data.get("refresh")


class ExamView(viewsets.ModelViewSet):

    serializer_class = ExamSerializer
    authentication_classes = [jwt_auth.JWTAuthentication]
    permission_classes = [IsExamAuthor]
    # queryset = Exam.objects.all()

    # def getq

    def get_queryset(self):
        # if setattr(self, "swagger_fake-view", False):
        user = self.request.user
        if user.is_authenticated:
            print(user)
            return Exam.objects.filter(user=user)
        raise exceptions.PermissionDenied()

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)


class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = [jwt_auth.JWTAuthentication]

    def has_permissions(self, request):
        permission_classes = []

        if self.action == "update" or "destroy":
            permission_classes = [IsQuestionAuthor]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            exam_id = self.validated_data["exam_id"]
            Exam = Exam.objects.filter(exam_id=exam_id)
            if Exam.user == user:
                return super().perform_create(self,serializer)
            raise exceptions.PermissionDenied()
        raise exceptions.NotAuthenticated()
