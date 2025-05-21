from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Count

def main(request):
    recipes = Recipe.objects.order_by('-created_at')[:5]
    context = { 'recipes': recipes }
    return render(request, 'main.html', context)

def category_list(request):
    categories_queryset = Category.objects.annotate(recipe_count=Count('categories'))
    categories_tuples = [(category.name, category.recipe_count) for category in categories_queryset]
    context = { 'categories': categories_tuples }
    return render(request, 'category_list.html', context)
