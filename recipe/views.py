from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def main(request):
    recipes = Recipe.objects.order_by('-created_at')[:5]
    context = { 'recipes': recipes }
    return render(request, 'main.html', context)
