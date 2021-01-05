# rest imports
from django.contrib.auth import get_user_model
from rest_framework import serializers

# django imports

# relative imports
from ..models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class GetUserSerializer(serializers.Serializer):
    username = serializers.CharField()