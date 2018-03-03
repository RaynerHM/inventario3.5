from django.shortcuts import render

# Create your views here.

#from .forms import RegForm
from .forms import FormCodigo, FormPassword
from .forms import FormAsignacion, FormPersonas

from django.contrib.auth.models import User
from .models import Registrado, Equipos, Personas

import code128
import os


# Create your views here.

#-- -------------------------- Vista Admin -------------------------- -->
"""def inicio1(request):
	form = RegForm(request.POST or None)
	if form.is_valid():
		form_data = form.cleaned_data
		abc = form_data.get("email")
		asd = form_data.get("nombre")
		obj = Registrado.objects.create(email=abc, nombre=asd)
	context = {
		"el_form": form,
	}
	return render(request, "index.html", context)
"""

#-- --------------------- Vista Generar Codigo --------------------- -->
def index(request):
	form = FormCodigo(request.POST)
	if form.is_valid():
		form_data = form.cleaned_data
		v_descripcion = form_data.get('descripcion')
		v_modelo = form_data.get("modelo")
		v_serial = form_data.get("serial")
		obj = Equipos.objects.create(descripcion=v_descripcion, 
		                            modelo=v_modelo, 
		                            serial=v_serial
		                            )
		ruta = r'static/imagen_codigo/'
		if not os.path.exists(ruta): os.makedirs(ruta)
		code128.image(v_descripcion + ' ' + v_modelo + ' ' +
						v_serial).save(ruta + v_serial + ".png")
	context = {
		"el_form": form,
	}
	return render(request, "index.html", context)


#-- --------------------- Vista Cambio de Clave --------------------- -->
def password(request):
	"""
	form = FormPassword(request.POST)
	if form.is_valid():
		form_data = form.cleaned_data
		v_pass_last = form_data.get("pass_last")
		v_rep_new = form_data.get("pass_new")
		

		#obj = User.objects.get(username='usuario')
		obj = User.objects.get(username = v_pass_last)
		obj.set_password(v_rep_new)
		obj.save()

	context = {
		"el_form": form,
	}
	return render(request, "password.html")
#-------------------------------------------------------------------------------

	form = FormPassword(request.POST)
	if form.is_valid():
		form_data = form.cleaned_data
		v_pass_last = form_data.get("pass_last")
		v_pass_new = form_data.get("pass_new")

		user = User.objects.get(username=v_pass_last)
		user.set_password(v_pass_new)
		user.save()

		if user.save():
			print('Excelente')
		else: 
			print('No se cambio')

	context = {
		"el_form": form,
	}
	"""
	return render(request, "password.html")




#-- --------------------- Vista Asignacion de Equipos --------------------- -->
def asignacion(request):
	"""
	form = FormAsignacion(request.POST)
	if form.is_valid():
		form_data = form.cleaned_data
		v_pass_last = form_data.get("pass_last")
		v_pass_new = form_data.get("pass_new")
		v_rep_pass = form_data.get("rep_pass")
		obj = Change_Pass.objects.create(pass_last=v_pass_last, 
		                                 pass_new=v_pass_new, 
		                                 rep_pass=v_rep_pass
		                                      )
	context = {
		"el_form": form,
	}
	return render(request, "asignacion.html", context)
	"""
	equipos = Equipos.objects.all()
	print(equipos)
	return render(request, "asignacion.html", 
	              {'result': equipos})


#-- --------------------- Vista Personas --------------------- -->
def persona(request):		
	form = FormPersonas(request.POST)
	if form.is_valid():
		form_data = form.cleaned_data
		v_nom_apel = form_data.get("nombre")
		v_depart = form_data.get("departamento")
		obj = Personas.objects.create(nombre=v_nom_apel, 
		                              departamento=v_depart, 
		                              )
	result = Personas.objects.all()
	context = {
		"el_form": form,
	              'result': result
	}
	return render(request, "persona.html", context)
	
	#return render(request, "persona.html")
	

