from django.shortcuts import render
from .models import PersonalPlan, FoodMainInformation

# Create your views here.

def index(request):
    """The home page of breakfast planner online"""
    return render(request, 'plan/index.html')

def personal_plans(request):
    """Show all plans"""
    personal_plans = PersonalPlan.objects.order_by()
    context = {'personal_plans':personal_plans}
    return render(request, 'plan/personal_plans.html', context)

def personal_plan(request, personal_plan_id):
    """Show all food labels and descriptions from oner personal plan"""
    personal_plan = PersonalPlan.objects.get(id=personal_plan_id)
    food_informations = personal_plan.foodmaininformation_set.all()    
    context = {'personal_plan':personal_plan, 'food_informations':food_informations}
    return render(request, 'plan/personal_plan.html', context)

