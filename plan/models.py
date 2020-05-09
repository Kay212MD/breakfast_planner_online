from django.db import models

# Create your models here.
class PersonalPlan(models.Model):
    """Name of the Plan"""
    plan_name = models.CharField(max_length=200)

    def __str__(self):
        """Returns name of plan name"""
        return self.plan_name

class FoodMainInformation(models.Model):
    """All main informations about the food"""
    perosnal_plan = models.ForeignKey(PersonalPlan, on_delete=models.CASCADE)
    food_label = models.CharField(max_length=200)
    food_description = models.TextField()
    # If food quantity is necessary the user have to input a number
    food_quantity_necessary = models.BooleanField()
    # if a reserve is necessary the creator have to input a number
    food_reserve_necessary = models.BooleanField()
    # If the value is zero, the calculated distribution factor is called
    maximum_distribution_of_food = models.IntegerField(default=0)

    def __str__(self):
        """Returns name of food label"""
        return f"{self.food_label}" #| {self.food_description[:20]}...



