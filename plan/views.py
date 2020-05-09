from django.shortcuts import render, redirect
from .models import PersonalPlan, FoodMainInformation
from .forms import PersonalPlanForm, FoodMainInformationForm

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

def new_personal_plan(request):
    """Add new personal plan"""
    if request != 'POST':
        # No data submitted, create a blank form
        form = PersonalPlanForm()
    else:
        # Post data submitted, process data
        form = PersonalPlanForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('plan:personal_plans')

    # Display a blank or invalid form.
    context={'form':form}
    return render(request, 'plan/new_personal_plan.html', context)

def new_food(request, personal_plan_id):
    """Add new food"""
    personal_plan = PersonalPlan.objects.get(id=personal_plan_id)

    if request != 'POST':
        # No data submitted, create a blank form
        form = FoodMainInformationForm()
    else:
        # Post data submitted, process data
        form = FoodMainInformationForm(data=request.POST)
        if form.is_valid():
            new_food = form.save(commit=False)
            new_food.personal_plan = personal_plan
            new_food.save()
            return redirect('plan:personal_plan', personal_plan_id=personal_plan_id)
    
    # Display a blank or invalid form.
    context={'personal_plan':personal_plan, 'form':form}
    return render(request, 'plan/new_food.html', context)



