from rest_framework import serializers
from api.models import Column, Todo


class TodoSerializer(serializers.ModelSerializer):
    idColumn = serializers.PrimaryKeyRelatedField(source='column', queryset=Column.objects.all())
    class Meta:
        model = Todo
        fields = ['id', 'name', 'idColumn']


class ColumnSerializer(serializers.ModelSerializer):
  todos = TodoSerializer(many=True, read_only=True) 
  class Meta:
    model=Column
    fields= '__all__'