from django import forms
from .models import PersonalPlan, FoodMainInformation

class PersonalPlanForm(forms.ModelForm):
    class Meta:
        model = PersonalPlan
        fields = ['plan_name']
        labels = {'plan_name':''}

class FoodMainInformationForm(forms.ModelForm):
    class Meta:
        model = FoodMainInformation
        fields = ['food_label',
                    'food_description',
                    'food_quantity_necessary',
                    'food_reserve_necessary', 
                    'maximum_distribution_of_food']
        labels = {'food_label':'food_label', 
                    'food_description':'food_description',
                    'food_quantity_necessary':'food_quantity_necessary',
                    'food_reserve_necessary':'food_reserve_necessary',
                    'maximum_distribution_of_food':'maximum_distribution_of_food'}
        