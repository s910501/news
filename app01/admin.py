from django.contrib import admin
from . import models

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(models.Question,QuestionAdmin)

