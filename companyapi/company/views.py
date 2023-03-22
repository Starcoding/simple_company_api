from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DepartmentSerializer, EmployeeSerializer
from .models import Department, Employee
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination


class EmployeePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 100


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get", "head"]


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed, edited.
    """

    pagination_class = EmployeePagination
    queryset = Employee.objects.select_related("department").all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["second_name", "department__id"]
    http_method_names = ["get", "post", "delete"]
