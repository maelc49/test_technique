from django.contrib import admin
from .models import Annonce

# Register your models here.

class AdminAnnonce(admin.ModelAdmin):
    list_display = ("departement", "ville", "code_ville", "prix")

admin.site.register(Annonce, AdminAnnonce)

