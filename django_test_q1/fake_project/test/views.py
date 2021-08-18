from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from django.db.models import Q

# Create your views here.

def infoPage(request):
    Employee_obj = Employee.objects.all()
    return render(request, 'hpage.html', {'Employee': Employee_obj} )

def postinfo(request):
    if(request.method == 'POST'):
        '''
        print(len(Employee.objects.all()))
        instance = Employee.objects.create()
        print(len(Employee.objects.all()))
        '''
        employee_name = request.POST.get("employee_name")
        instance = Employee(Employee_name =employee_name,  Employee_department = "HR")
        
        instance.save()
        Employee_obj = Employee.objects.all() 

        return render(request, 'hpage.html', {'Employee': Employee_obj})

def delinfo(request, id):
    Employee.objects.filter(id=id).delete()
    Employee_obj = Employee.objects.all() 
    return render(request, 'hpage.html', {'Employee': Employee_obj})
    #SomeModel.objects.filter(id=id).delete()