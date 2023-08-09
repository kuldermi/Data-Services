from rest_framework import serializers
from. import models

# class StudentMergedSerializer( serializers.ModelSerializer ):
#     class Meta:
#         model = models.Students
#         exclude = ('studentId',)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Students
        fields= '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = '__all__'


class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentStandard
        fields = '__all__'

class StudentTeacherSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only = True, many = True)
    class Meta:
        model = models.Teacher
        fields = '__all__'