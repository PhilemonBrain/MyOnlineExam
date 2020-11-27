from django.urls import path
from .views import UserView, SingleUserView, SignUp
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('users/<int:pk>/', SingleUserView.as_view(), name='single_user'),
    path('signup', SignUp.as_view(), name="signup"),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]