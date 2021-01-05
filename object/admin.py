# django imports
from django.contrib import admin

# relative imports
from .models import Todo

admin.site.register(Todo)