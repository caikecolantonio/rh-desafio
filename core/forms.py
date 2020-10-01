from django import forms
from .models import Employee



class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','user','gender', 'phone', 'role', 'age', 'joining_date', 'salary', 'department']