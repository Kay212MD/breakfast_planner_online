from django import forms
from .models import PersonalPlan

class PersonalPlanForm(forms.ModelForm):
    class Meta:
        model = PersonalPlan
        fields = ['plan_name']
        labels = {'plan_name':''}
