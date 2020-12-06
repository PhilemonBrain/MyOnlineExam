from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import get_user_model as User
from rest_framework import status, views, generics, authentication, permissions, decorators, viewsets, exceptions
from rest_framework.response import Response
from .serializers import UserSerializer, ExamSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt import authentication as jwt_auth
# from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from .models import Exam

class IsExamAuthor(permissions.BasePermission):
    # this is a custom permission to reatrict access to CRUD of another users exam
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)


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
    # permission_classes = (permissions.IsAuthenticated,)
    # queryset = Exam.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Exam.objects.filter(user=user)
        raise exceptions.PermissionDenied()

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)


class QuestionView(views.APIView):
    #expecting an array of all the options in an 'option' field in the request.data
    def post(self, request, *args, **kwargs):
        # we = request.data
        question_title = request.data.get("title")
        answer = request.data.get("answer")
        optionA = request.data.get("optionA")
        optionB = request.data.get("optionB")
        optionC = request.data.get("optionC")
        optionD = request.data.get("optionD")
        optionE = request.data.get("optionE")
        # we still need to find a way to get the exam_id for this request
        exam_id = request.data.get("exam_id")
        exam = Exam.objects.get(id=exam_id)
        return Response({"Response": "data"}, status=status.HTTP_200_OK)


# class TestTokenView(views)