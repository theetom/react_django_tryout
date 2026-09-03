from django.urls import path
from . import views


urlpatterns = [
    path("recipes/", views.recipe_list),
    path("recipes/<str:recipe_name>/", views.recipe_detail),
]