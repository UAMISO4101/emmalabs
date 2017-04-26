# coding=utf-8
# Modelo de perfil de usuario que extiende al usuario Django
from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm


class Rol(models.Model):
    rol = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=2000, null=False)


class Usuario(models.Model):
    # Referencia al usuario de Django
    user = models.ForeignKey(User)
    # Atributos extra
    nombres = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=50, null=False)
    pais = models.CharField(max_length=50, null=True)
    ciudad = models.CharField(max_length=50, null=True)
    intereses = models.CharField(max_length=200, null=False)
    rol_usuario = models.ForeignKey(Rol)

    def __str__(self):
        return '{}'.format(self.nombres)


class OpcionMenu(object):
    opcion = ''
    template = ''


class ItemMenu(object):
    menu = ''
    opciones = []


class MenuPorRol(models.Model):
    rol = models.ForeignKey(Rol)
    menu = models.CharField(max_length=100, null=False)
    opcion = models.CharField(max_length=100, null=False)
    template = models.CharField(max_length=500, null=False)

    class Meta:
        unique_together = ('rol', 'menu', 'opcion')


class LoginForm(ModelForm):
    username_login = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Usuario'
    )
    password_login = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Contraseña'
    )

    class Meta:
        model = User
        fields = ['username_login', 'password_login']
