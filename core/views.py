from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm



# Create your views here.

# Criar

def ProcessCreate(request):
    form = EmployeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return "foi"

    return render(request, 'core/forms.html', {'form': form})

#Ver cadastrados

def ProcessList(request):
    employee = Employee.objects.all()
    return render(request, 'core/todos.html', {'employee': employee})

#Editar cadastrados

def ProcessUpdate(request, id):
    employee = Employee.objects.get(pk=id)
    form = EmployeeForm(request.POST or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('core:process-list')

    return render(request, 'core/forms.html', {'form':form , 'employee':employee})

#Deletar cadastradps

def ProcessDelete(request, id):
    employee = Employee.objects.get(id=id)

    if request.method == 'POST':
        employee.delete()
        return redirect('core:process-list')

    return render(request, 'core/delete.html', {'employee':employee})