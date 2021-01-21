from dmdbBaseManagement.models import Employee, Tutor, Student
from rest_framework import serializers
from dmdbBaseManagement.models import GodParent


class GodParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GodParent
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
