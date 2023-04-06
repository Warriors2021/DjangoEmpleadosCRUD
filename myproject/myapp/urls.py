from django.urls import path
from .views import DepartamentoList, DepartamentoDetail, EmpleadoList, EmpleadoDetail


urlpatterns = [
    path('departamentos/', DepartamentoList.as_view(), name='departamento-list'),
    path('departamentos/<int:pk>/', DepartamentoDetail.as_view(), name='departamento-detail'),
    path('empleados/', EmpleadoList.as_view(), name='empleado-list'),
    path('empleados/<int:pk>/', EmpleadoDetail.as_view(), name='empleado-detail'),
]
