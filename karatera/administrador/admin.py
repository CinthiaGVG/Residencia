from django.contrib import admin
from .models import GeneroModel,EdadModel,NivelModel,Cinta_NivelModel,ClasificacionKarateModel,DisciplinaModel

# Register your models here.
class SexoAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")
class EdadAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")
class NivelAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")
class Cinta_NivelAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")
class ClasificacionKarateAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")
class DiciplinaAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")

admin.site.register(GeneroModel,SexoAdmin)
admin.site.register(EdadModel,EdadAdmin)
admin.site.register(NivelModel,NivelAdmin)
admin.site.register(Cinta_NivelModel,Cinta_NivelAdmin)
admin.site.register(ClasificacionKarateModel,ClasificacionKarateAdmin)
admin.site.register(DisciplinaModel,DiciplinaAdmin)