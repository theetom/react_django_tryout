from rest_framework import serializers
from .models import Recipe, RecipeIngredient, Category
from reviews.models import Review

class RecipeIngredientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="ingredient.name")

    class Meta:
        model = RecipeIngredient
        fields = ["name", "quantity", "unit"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "comment", "grade", "timestamp"]

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(
        source="recipe_ingredients",
        many=True
    )

    categories = CategorySerializer(
        many=True
    )
    reviews = ReviewSerializer(
        many=True
    )

    class Meta:
        model = Recipe
        fields = [
            "id",
            "title",
            "description",
            "date_created",
            "user",
            "ingredients",
            "categories",
            "reviews",
        ]