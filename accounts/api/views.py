# rest_framework imports
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# django imports
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict

# relative imports
from .serializers import UserSerializer


CustomUser = get_user_model()


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class LoggedInUser(APIView):
    def get(self, request):
        user_info = model_to_dict(CustomUser.objects.get(username=request.user))
        return Response(user_info, status=status.HTTP_200_OK)

