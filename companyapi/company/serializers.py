from . import models
from django.db.models import Count, Sum
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    number_of_employees = serializers.SerializerMethodField("get_number_of_employees")
    salaries = serializers.SerializerMethodField("get_salaries")

    def get_number_of_employees(self, obj):
        return (
            models.Employee.objects.select_related("department")
            .filter(department=obj)
            .count()
        )

    def get_salaries(self, obj):
        return (
            models.Employee.objects.select_related("department")
            .filter(department=obj)
            .aggregate(Sum("salary"))["salary__sum"]
        )

    class Meta:
        model = models.Department
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = "__all__"
