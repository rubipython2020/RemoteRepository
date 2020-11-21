from django import forms
from .models import Employee
class employeeform(forms.ModelForm):
    class Meta:
        model=Employee
        fields={'fullname','mobile','emp_code','position'}
        labels={
            'fullname':'Full Name',
            'emp_code':'Emp Code'
        }

    def __init__(self,*args,**kwargs):
        super(employeeform,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label='--select--'