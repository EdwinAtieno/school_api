from rest_framework import serializers
from teacher.models import *


class TeacherSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.CharField(max_length=26)
    Tid = serializers.CharField(max_length=26)
    D_O_E = serializers.DateTimeField(required=True)
    Department = serializers.ChoiceField(choices=Deps,required=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Teachers.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.Tid = validated_data.get('Tid', instance.Tid)
        instance.D_O_E = validated_data.get('D_O_E', instance.D_O_E)
        instance.Department = validated_data.get('Department', instance.Department)
        instance.save()
        return instance

