from .models import LocDepartment
from .serializers import LocDepartmentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



class LocDepartmentModelViewSet(viewsets.ModelViewSet):
    queryset = LocDepartment.objects.all()
    serializer_class = LocDepartmentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class LocDepartmentLocIDModelViewSet(viewsets.ModelViewSet):
    serializer_class = LocDepartmentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self, *args, **kwargs):
        qs = LocDepartment.objects.all()
        location_id = self.kwargs['location_id']
        if location_id is not None:
            return qs.filter(location=location_id)
        else:
            return qs

class LocDepartmentLocIDDeptIDModelViewSet(viewsets.ModelViewSet):
    serializer_class = LocDepartmentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self, *args, **kwargs):
        qs = LocDepartment.objects.all()
        location_id = self.kwargs['location_id']
        department_id = self.kwargs['department_id']
        if location_id and department_id is not None:
            return qs.filter(location=location_id, department=department_id)
        else:
            return qs
          