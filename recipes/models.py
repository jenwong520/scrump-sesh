from django.db import models
from django.conf import settings

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    picture = models.URLField(max_length=500, blank=True, null=True) # image is optional
    description = models.TextField()
    difficulty_level = models.CharField(
        max_length=20,
        choices=[("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard")],
        default="Easy",
    )
    prep_time = models.PositiveIntegerField(help_text="Time in minutes", null=True, blank=True)
    cook_time = models.PositiveIntegerField(help_text="Time in minutes", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="recipes",
        on_delete=models.CASCADE,
        null=True
    )

    def total_time(self):
        return (self.prep_time or 0) + (self.cook_time or 0)

    def __str__(self):
        return self.title

class RecipeStep(models.Model):
    step_number = models.PositiveSmallIntegerField()
    instruction = models.TextField()
    recipe = models.ForeignKey(
        Recipe,
        related_name="steps",
        on_delete=models.CASCADE,
    )
    class Meta:
        ordering = ["step_number"]

class FoodItem(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    amount = models.CharField(max_length=100)
    food_item = models.ForeignKey(
        FoodItem,
        on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(
        Recipe,
        related_name="ingredients",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["food_item"]
