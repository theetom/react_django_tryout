from urllib import request

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Recipe
from .serializers import RecipeSerializer, ReviewSerializer


@api_view(["GET", "POST"])
def recipe_list(request):

    # GET /api/recipes/
    if request.method == "GET":
        recipes = Recipe.objects.all()

        serializer = RecipeSerializer(
            recipes,
            many=True
        )

        return Response(serializer.data)


    # POST /api/recipes/
    if request.method == "POST":

        serializer = RecipeSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(["GET", "POST"])
def recipe_detail(request, recipe_name):

    try:
        recipe = Recipe.objects.get(title=recipe_name)
    except Recipe.DoesNotExist:
        return Response(
            {"error": "Recipe not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    if request.method == "POST":
        if not request.user.is_authenticated:
            return Response(
                {"error": "You must be logged in to write a review."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(
                recipe=recipe,
                user=request.user
            )
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

""" import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from .models import (
    Recipe,
    Category,
    Ingredient,
    RecipeIngredient,
    RecipeStep,
)


@api_view(["GET"])
def home(request):
    return Response({
        "message": "Recipe API is working!"
    })

@csrf_exempt
def create_recipe(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST allowed"},
            status=405
        )

    data = json.loads(request.body)

    user, created = User.objects.get_or_create(
        username="test_user"
    )

    recipe = Recipe.objects.create(
        title=data["title"],
        description=data.get("description", ""),
        user=user,
    )

    for category_name in data.get("categories", []):
        category, created = Category.objects.get_or_create(
            name=category_name
        )

        recipe.categories.add(category)

    for item in data.get("ingredients", []):
        ingredient, created = Ingredient.objects.get_or_create(
            name=item["name"]
        )

        RecipeIngredient.objects.create(
            recipe=recipe,
            ingredient=ingredient,
            quantity=item["quantity"],
            unit=item["unit"],
        )

    for step in data.get("steps", []):
        RecipeStep.objects.create(
            recipe=recipe,
            step_number=step["step_number"],
            instruction=step["instruction"],
        )

    return JsonResponse({
        "message": "Recipe created successfully",
        "recipe_id": recipe.id
    }, status=201) """