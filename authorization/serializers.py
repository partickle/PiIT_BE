from rest_framework import serializers

from authorization import models


class TeacherLoginSerializer(serializers.Serializer):
    usertag = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = models.Teacher
        fields = ('usertag', 'password')

