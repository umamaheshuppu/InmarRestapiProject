from rest_framework import serializers
from .models import LocDepartment

class LocDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocDepartment
        fields = "__all__"