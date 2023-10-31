from django.contrib import admin

# Register your models here.
# STEP 9: import models from Question to have an admin interface
from .models import Question

admin.site.register(Question)