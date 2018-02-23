from django import forms
from .models import Registrado, Equipos, Personas

#from .models import Equipos
#from .models import Personas

#-- --------------------- Formulario Admin ------------------------------------- -->
class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["nombre", "email"]
		
	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, proveeder = email.split("@")
		dominio, extension = proveeder.split(".")
		if not extension == "edu":
			raise forms.ValidationError("Solo correos .EDU")
		return email
class RegForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	email = forms.EmailField()


#-- --------------------- Formulario Generar codigo ---------------------------- -->
	#-- ----- Recibir Datos ----- -->
class FormCodigo(forms.ModelForm):
	class Meta:
		model = Equipos
		fields = ["descripcion", "modelo", "serial"]
class RegFormCodigo(forms.Form):
	descripcion = forms.CharField(max_length=30)
	modelo = forms.CharField(max_length=30)
	serial = forms.CharField(max_length=30)

#-- ----- Mostrar Imagen ----- -->



#-- --------------------- Formulario Cambio de Clave --------------------------- -->
#-- ----- Recibir Datos ----- -->
class FormPassword(forms.ModelForm):
	"""class Meta:
		model = Codigo_de_Barras
		fields = ["pass_last", "pass_new"]"""
class RegFormPassword(forms.Form):
	pass_last = forms.CharField(max_length=30)
	pass_new = forms.CharField(max_length=30)



#-- --------------------- Formulario Asignacion de Equipos --------------------- -->
#-- ----- Recibir Datos ----- -->
class FormAsignacion(forms.ModelForm):
	"""class Meta:
		model = Codigo_de_Barras
		fields = ["descripcion", "modelo", "serial"]"""
class RegFormAsignacion(forms.Form):
	descripcion = forms.CharField(max_length=30)
	modelo = forms.CharField(max_length=30)
	serial = forms.CharField(max_length=30)



#-- ---------------------------- Formulario Personas ---------------------------- -->
#-- ----- Recibir Datos ----- -->
class FormPersonas(forms.ModelForm):
	class Meta:
		model = Personas
		fields = ["nombre", "departamento"]
class RegFormPersonas(forms.Form):
	nombre = forms.CharField(max_length=50)
	departamento = forms.CharField(max_length=50)
