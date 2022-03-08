from django.shortcuts import render
from testapp.models import employee
from testapp.forms import employeeform
from django.http import HttpResponseRedirect
import requests
# Create your views here.

def index_view(request):
    employees=employee.objects.all()
    return render(request,'index.html',{'employees':employees})

def create_view(request):
    form=employeeform()
    if request.method=='POST':
        form=employeeform(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    return render(request,'create.html',{'form':form})

def delete_view(request,id):
    employees=employee.objects.get(id=id)
    employees.delete()
    return HttpResponseRedirect('/')

def update_view(request,id):
    employees=employee.objects.get(id=id)
    if request.method=='POST':
        form=employeeform(request.POST,instance=employees)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    return render(request,'update.html',{'employees':employees})
