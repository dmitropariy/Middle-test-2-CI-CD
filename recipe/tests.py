from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .models import Category, Recipe


class CategoryModelTests(TestCase):

    def setUp(self):
        # Створюємо тестову категорію
        self.category = Category.objects.create(name="Тестова категорія")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Тестова категорія")
        self.assertTrue(isinstance(self.category, Category))

    def test_category_str_method(self):
        self.assertEqual(str(self.category), "Тестова категорія")

    def test_category_iter_method(self):
        # Створюємо кілька рецептів для категорії
        recipe1 = Recipe.objects.create(
            title="Рецепт 1",
            description="Опис рецепту 1",
            instructions="Інструкції для рецепту 1",
            ingredients="Інгредієнти для рецепту 1",
            category=self.category
        )

        recipe2 = Recipe.objects.create(
            title="Рецепт 2",
            description="Опис рецепту 2",
            instructions="Інструкції для рецепту 2",
            ingredients="Інгредієнти для рецепту 2",
            category=self.category
        )

        # Перевіряємо роботу ітератора
        recipes = list(self.category)
        self.assertEqual(len(recipes), 2)
        self.assertIn(recipe1, recipes)
        self.assertIn(recipe2, recipes)