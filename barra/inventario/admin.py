from django.contrib import admin

# Register your models here.


from .models import Registrado

from .models import Equipos
from .models import Personas

from .models import Equipos1
from .models import Personas1

class AdminRegistrado(admin.ModelAdmin):
	#list_display = ["__unicode__","nombre","timestamp"]
	list_display = ["email","nombre","timestamp"]

	class Meta:
		model = Registrado

admin.site.register(Registrado, AdminRegistrado)



class AdminCodigo(admin.ModelAdmin):
	list_display = ["descripcion", "modelo", "serial"]

	class Meta:
		model = Equipos

admin.site.register(Equipos, AdminCodigo)



class AdminPersonas(admin.ModelAdmin):
	list_display = ["nombre", "departamento"]

	class Meta:
		model = Personas

admin.site.register(Personas, AdminPersonas)




#----------------------------------------------------------
admin.site.register(Equipos1)
admin.site.register(Personas1)
