# rest imports
from rest_framework import serializers

# django imports

# relative imports
from ..models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
