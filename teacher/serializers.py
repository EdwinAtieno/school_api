from rest_framework import serializers
from teacher.models import *


class TeacherSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.CharField(max_length=26)
    name = serializers.CharField(max_length=26)
    Date_Of_Birth = serializers.DateTimeField(required=True)
    age = serializers.IntegerField()
    gender = serializers.ChoiceField(choices=genders, required=True)
    role = serializers.ChoiceField(choices=roles,required=True)


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
        instance.name = validated_data.get('name', instance.name)
        instance.Date_Of_Birth = validated_data.get('Date_Of_Birth', instance.Date_Of_Birth)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance

