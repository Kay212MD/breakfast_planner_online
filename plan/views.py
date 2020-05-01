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
    # food_descriptions = FoodMainInformation.objects.values('food_description')
    # Try to get food description, not only as Query
    # food_main =FoodMainInformation.objects.all()
    # food_description_list =[]
    # for food_id_search in food_main:
    #     food_id = food_id_search.id
    #     food_id_reference = FoodMainInformation.objects.get(id=food_id)
    #     food_description_list.append(food_id_reference.food_description)
    #food_descriptions = FoodMainInformation.food_description
    context = {'personal_plan':personal_plan, 'food_informations':food_informations}
    return render(request, 'plan/personal_plan.html', context)

