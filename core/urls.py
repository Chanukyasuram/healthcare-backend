from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import add_patient_page, add_doctor_page

from .views import (
    RegisterView, MyTokenObtainPairView,
    PatientListCreateView, PatientRetrieveUpdateDeleteView,
    DoctorListCreateView, DoctorRetrieveUpdateDeleteView,
    MappingListCreateView, MappingByPatientView,
    home, user_dashboard, admin_dashboard,
    patients_page, doctors_page
)

urlpatterns = [
    path('', home, name='home'),

    # Auth
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', MyTokenObtainPairView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Dashboards
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),

    # Pages under dashboard/
    path('dashboard/patients.html', patients_page, name='patients_page'),
    path('dashboard/doctors.html', doctors_page, name='doctors_page'),

    # Patients API
    path('patients/', PatientListCreateView.as_view(), name='patients-list-create'),
    path('patients/<int:pk>/', PatientRetrieveUpdateDeleteView.as_view(), name='patients-rud'),

    # Doctors API
    path('doctors/', DoctorListCreateView.as_view(), name='doctors-list-create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDeleteView.as_view(), name='doctors-rud'),

    



    # Mappings API
    path('mappings/', MappingListCreateView.as_view(), name='mappings-list-create'),
    path('mappings/<int:patient_id>/', MappingByPatientView.as_view(), name='mappings-by-patient'),
]
