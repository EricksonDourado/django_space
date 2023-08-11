from django.contrib import admin
from galeria.models import Fotografia

class config_gride_fotografia(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")
    list_display_links = ("id","nome",)
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_per_page = 1


admin.site.register(Fotografia,config_gride_fotografia)

# Register your models here.
