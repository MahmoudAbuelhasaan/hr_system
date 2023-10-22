

from .models import HR
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
import json

# import logout





@csrf_exempt
def hr_register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        email = data['email']
        password = data['password']
        hr = HR(name=name, email=email,password=password)
        hr.save()
        return JsonResponse({"message": "HR has been registered"})

@csrf_exempt
def hr_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['email']
        password = data['password']
        try:
            hr = HR.objects.get(email=email)
            if hr:
                # check password
                if hr.password == password:

                    response_data = {
                        "message": "HR has been logged in",
                        "uid": hr.id,
                        "name": hr.name
                    }
                    return JsonResponse(response_data)
                else:
                    return JsonResponse({"message": "Incorrect Password"})
            else:
                return JsonResponse({"message": "HR not found"})
        except HR.DoesNotExist:
            return JsonResponse({"message": "HR not found"})
    else:
        return JsonResponse({"message": "Invalid method"})


from django.http import JsonResponse, HttpResponse
from .models import Employee, Attendance

def add_employee(request):
    if request.method == 'POST':
        data = request.POST  # Assumes you are sending data as form data
        name = data.get('name')
        email = data.get('email')
        employee_id = data.get('employee_id')
        department = data.get('department')

        # Validate and create a new employee
        if name and email and employee_id and department:
            employee = Employee(name=name, email=email, employee_id=employee_id, department=department)
            employee.save()
            return JsonResponse({"message": "Employee added successfully"})
        else:
            return JsonResponse({"message": "Incomplete data provided"}, status=400)

def edit_employee(request, employee_id):
    if request.method == 'PUT':
        try:
            employee = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            return JsonResponse({"message": "Employee not found"}, status=404)

        data = request.PUT  # Use request.PUT or request.POST based on your form data
        # Update employee fields here

        employee.save()
        return JsonResponse({"message": "Employee updated successfully"})

def add_attendance(request):
    if request.method == 'POST':
        data = request.POST
        employee_id = data.get('employee_id')
        date = data.get('date')
        status = data.get('status')

        try:
            employee = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            return JsonResponse({"message": "Employee not found"}, status=404)

        # Validate and create a new attendance record
        if date and status:
            attendance = Attendance(employee=employee, date=date, status=status)
            attendance.save()
            return JsonResponse({"message": "Attendance added successfully"})
        else:
            return JsonResponse({"message": "Incomplete data provided"}, status=400)

