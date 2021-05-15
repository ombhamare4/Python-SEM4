from django.forms import ModelForm
from .models import Student

class CreateStudentForm(ModelForm):
    class Meta:
        model=Student
        fields=['student_name','age','department','current_sem','address','cgpi']