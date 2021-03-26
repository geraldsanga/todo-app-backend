# rest imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

# django imports

# relative imports
from .serializers import TodoSerializer
from ..models import Todo


class TodoApi(APIView):
    def get(self, request):
        print(request.user)
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