from django.contrib import admin
from .models import Question, Choix

# Register your models here.

admin.site.register(Question)
admin.site.register(Choix)
