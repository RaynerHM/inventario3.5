from django.db import models

# Create your models here.


class Registrado(models.Model):
	nombre = models.CharField(max_length=100, blank=False, null=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.email

	def __str__(self):
		return self.email
		

class Equipos(models.Model):
	descripcion = models.CharField(max_length=100, blank=False, null=False)
	modelo = models.CharField(max_length=100, blank=False, null=False)
	serial = models.CharField(max_length=100, blank=False, null=False)
	#id_persona = models.CharField(max_length=20, blank=True, null=True)
	id_persona = models.ForeignKey(
		'Personas', on_delete=models.CASCADE, blank=True, null=True)
	#imagen = models.URLField()



class Personas(models.Model):
	#nombre = models.ManyToManyField(Equipos1)
	nombre = models.CharField(max_length=50, blank=False, null=False)
	departamento = models.CharField(max_length=50, blank=False, null=False)
	
	def prueba(self):
		return self.nombre

	def __str__(self):
		return self.nombre


"""
class 
class Change_Pass(models.Model):
	descripcion = models.CharField(max_length=100, blank=False, null=False)
	modelo = models.CharField(max_length=100, blank=False, null=False)
	serial = models.CharField(max_length=100, blank=False, null=False)
	#imagen = models.URLField()
"""
