from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Recipe
from .serializers import RecipeSerializer


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

@api_view(["GET"])
def home(request):
    return Response({
        "message": "Recipe API is working!"
    })
