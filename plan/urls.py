"""Defines URL patterns for plan"""

from django.urls import path

from . import views

app_name = 'plan' 
urlpatterns = [
    # Home page
    path('', views.index, name = 'index'),
    # Page that will show the plans
    path('personal_plans', views.personal_plans, name = 'personal_plans'),
    # Page that will show all food labels of a single Plan
    path('personal_plans/<int:personal_plan_id>/', views.personal_plan, 
        name='personal_plan'),
    # Page for adding a new plan
    path('new_personal_plan', views.new_personal_plan, name='new_personal_plan'),
    # Page for adding new food
    path('new_food/<int:personal_plan_id>/', views.new_food, name='new_food'),
    ]
