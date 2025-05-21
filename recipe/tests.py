from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .models import Category, Recipe


class CategoryModelTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Тестова категорія")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Тестова категорія")
        self.assertTrue(isinstance(self.category, Category))

    def test_category_str_method(self):
        self.assertEqual(str(self.category), "Тестова категорія")

    def test_category_iter_method(self):
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

        recipes = list(self.category)
        self.assertEqual(len(recipes), 2)
        self.assertIn(recipe1, recipes)
        self.assertIn(recipe2, recipes)


class RecipeModelTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Тестова категорія")

        self.recipe = Recipe.objects.create(
            title="Тестовий рецепт",
            description="Опис тестового рецепту",
            instructions="Крок 1. Змішати\nКрок 2. Запекти",
            ingredients="Яйця - 2 шт.\nМолоко - 200 мл",
            category=self.category
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, "Тестовий рецепт")
        self.assertEqual(self.recipe.description, "Опис тестового рецепту")
        self.assertTrue(isinstance(self.recipe, Recipe))
        self.assertEqual(self.recipe.category, self.category)

    def test_recipe_str_method(self):
        self.assertEqual(str(self.recipe), "Тестовий рецепт")

    def test_recipe_created_at_field(self):
        self.assertIsNotNone(self.recipe.created_at)
        self.assertLess(timezone.now() - self.recipe.created_at, timedelta(seconds=10))

    def test_recipe_updated_at_field(self):
        original_updated_at = self.recipe.updated_at

        self.recipe.title = "Оновлений тестовий рецепт"
        self.recipe.save()

        self.assertNotEqual(original_updated_at, self.recipe.updated_at)

    def test_recipe_category_relationship(self):
        self.assertEqual(self.recipe.category.name, "Тестова категорія")

        category_recipes = list(self.category.categories.all())
        self.assertIn(self.recipe, category_recipes)