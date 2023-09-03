from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import APIView
#from rest_framework.exceptions import PermissionDenied

from .models import *
from .serializers import *


#class IsUser(permissions.BasePermission):
#
#    def has_object_permission(self, request, view, obj):
#        return obj.User == request.User


#class Logout(APIView):
#
#    def get(self, request, format=None):
#        request.User.auth_token.delete()
#        return Response(status=status.HTTP_200_OK)
#
#
#class UserRetrieveView(generics.RetrieveAPIView):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#    #permission_class = permissions.IsAuthenticatedOrReadOnly
#
#
#class UserUpdateView(generics.UpdateAPIView):
#    queryset = User.objects.all()
#    serializer_class = CreateUserSerializer
#
#
#class UserCreateView(generics.CreateAPIView):
#    queryset = User.objects.all()
#    serializer_class = CreateUserSerializer
#
#
#class UserListView(generics.ListAPIView):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
