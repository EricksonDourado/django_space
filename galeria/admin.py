from django.contrib import admin
from galeria.models import Fotografia

class config_gride_fotografia(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")
    list_display_links = ("id","nome",)
    search_fields = ("nome",)


admin.site.register(Fotografia,config_gride_fotografia)

# Register your models here.
