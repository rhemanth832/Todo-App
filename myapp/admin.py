from django.contrib import admin
from .models import Todoitem

# Register your models here.
admin.site.register(Todoitem)
# This code registers the Todoitem model with the Django admin site, allowing it to be managed through the admin interface.