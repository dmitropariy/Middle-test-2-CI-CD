from django.contrib import admin
from django.urls import path

import recipe.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', recipe.views.main, name='main'),
]