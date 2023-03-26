from django.contrib import admin
from . models import Categoria, Donacion, Beneficiario, Ciudad
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
	readonly_fields=("created","updated")

class DonacionAdmin(admin.ModelAdmin):
	readonly_fields=("created", "updated")

class BeneficiarioAdmin(admin.ModelAdmin):
	readonly_fields=("created", "updated")

class CiudadAdmin(admin.ModelAdmin):
	readonly_fields=("created", "updated")

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Donacion, DonacionAdmin)
admin.site.register(Beneficiario, BeneficiarioAdmin)
admin.site.register(Ciudad, CiudadAdmin)