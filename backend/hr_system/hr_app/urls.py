from django.urls import path
from . import views

urlpatterns = [
    # register path
    path('hr_register/',views.hr_register,name='hr_register'),
    # login path
    path('hr_login/',views.hr_login,name='hr_login'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('edit_employee/<str:employee_id>/', views.edit_employee, name='edit_employee'),
    path('add_attendance/', views.add_attendance, name='add_attendance'),
 

]
