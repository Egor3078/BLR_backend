from django.urls import path, include
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),
    #path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('users/<int:pk>', UserRetrieveView.as_view()),
    #path('users/update/<int:pk>', UserUpdateView.as_view()),
    #path('users/all', UserListView.as_view()),
    #path('users/new', UserCreateView.as_view()),
]