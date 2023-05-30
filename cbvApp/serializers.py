from rest_framework import serializers

from cbvApp.models import Student


class StudentSerializer(serializers.ModelSerializer):
    model = Student
    fields = ['id', 'name', 'score']
