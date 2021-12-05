from rest_framework import serializers
from student.models import *


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.CharField(max_length=26)
    Sid = serializers.CharField(max_length=26)
    Class = serializers.CharField(max_length=25)
    Dormitory = serializers.ChoiceField(choices=doms,required=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Students.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.Sid = validated_data.get('Sid', instance.name)
        instance.Class = validated_data.get('Class', instance.age)
        instance.Dormitory = validated_data.get('Dormitory', instance.gender)
        instance.save()
        return instance

