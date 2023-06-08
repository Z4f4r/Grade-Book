from rest_framework import serializers
from .models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    student = StudentSerializer()

    class Meta:
        model = Grade
        fields = '__all__'
