from django.urls import path
from recipes.views import recipe_list, show_recipe, create_recipe, edit_recipe

urlpatterns = [
    path("", recipe_list, name="recipe_list"),
    path("<int:id>/", show_recipe, name="show_recipe"),
    path("create/", create_recipe, name="create_recipe"),
    path("<int:id>/edit/", edit_recipe, name="edit_recipe"),
]
