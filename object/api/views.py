# rest imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

# django imports
from django.contrib.auth import get_user_model

# relative imports
from .serializers import TodoSerializer, GetUserSerializer
from ..models import Todo


class TodoApi(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        todo_serializer = TodoSerializer(data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(todo_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(todo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoRoutes(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        todo_serializer = TodoSerializer(todo)
        return Response(todo_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        todo_serializer = TodoSerializer(instance=todo, data=request.data)

        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(todo_serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(todo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        todo.delete()

        return Response(headers={'deleted': 'The request was excecuted'}, status=status.HTTP_204_NO_CONTENT)


class UserInformationView(APIView):
    def post(self, request):
        user_serializer = GetUserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = get_object_or_404(get_user_model(), username=user_serializer.validated_data['username'])
            user_info = {
                'username': user.username,
                'email_address': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
            return Response(user_info, status=status.HTTP_200_OK)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
