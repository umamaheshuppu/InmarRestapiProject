from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

routers=DefaultRouter()
routers.register(r'v1/location',views.LocDepartmentModelViewSet,basename='LocDepartment')
# routers.register(r'location/{location_id}/department',views.LocDepartmentIDModelViewSet,basename='LocDepartmentID')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/location/<str:location_id>/department',views.LocDepartmentLocIDModelViewSet.as_view({'get': 'list'}), name='LocDepartmentLocID'),
    path('v1/location/<str:location_id>/department/<str:department_id>/category',views.LocDepartmentLocIDDeptIDModelViewSet.as_view({'get': 'list'}), name='LocDepartmentLocIDDeptID'),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
    path('',include(routers.urls)),
]

# urlpatterns = [
#     path('location', views.LocDepartmentModelViewSet.as_view({'get': 'list'})),
# ]
