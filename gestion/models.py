from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .authManager import UsuarioManager
# Create your models here.

class UsuarioModel(AbstractBaseUser,PermissionsMixin):
    id = models.AutoField(primary_key=True,unique=True, null=False)
    nombre = models.CharField(max_length=15,null=False)
    apellido = models.CharField(max_length=15,null=False)
    correo = models.EmailField(max_length=50,unique=True,null=False)
    password=models.TextField(null=False)
    tipoUsuario=models.CharField(max_length=13,choices=[
        ('ADMIN','ADMINISTRADOS'),
        ('USER','USUARIO')
    ],db_column='tipo_usuario', default='USER')
    is_staff = models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    createdAt=models.DateTimeField(auto_now_add=True,db_column='created_at')
    
    objects = UsuarioManager()
    USERNAME_FIELD='correo'
    REQUIRED_FIELDS=['nombre','apellido','tipoUsuario','password']

    class Meta: 
        db_table = 'usuarios'

class CineModel(models.Model):
    id = models.AutoField(primary_key=True,null=False,unique=True)
    direccion = models.CharField(max_length=50,null=False,unique=True)
    cantSalas = models.IntegerField(null=False)
    fechaCreacion = models.DateTimeField(auto_now_add=True,db_column='fecha_creacion',null=False)

    class Meta:
        db_table='cines'

class PeliculaModel(models.Model):
    id = models.AutoField(primary_key=True,null=False,unique=True)
    peliculas = models.CharField(max_length=50,unique=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True,db_column='fecha_creacion',null=False)

    class Meta:
        db_table='peliculas'

class SalaModel(models.Model):
    id = models.AutoField(primary_key=True,null=False,unique=True)
    id_sala = models.CharField(max_length=10,unique=True,null=False)
    cantAsientos = models.IntegerField(null=False)
    duracion = models.TimeField(null=False)
    id_pelicula = models.ForeignKey(PeliculaModel,to_field='id',on_delete=models.CASCADE)
    cine = models.ForeignKey(CineModel,to_field='id',on_delete=models.CASCADE)

    class Meta:
        db_table='salas'

class AsientoModel(models.Model):
    id = models.AutoField(primary_key=True,null=False,unique=True)
    id_asiento = models.CharField(max_length=2,unique=False,null=False)
    disponibilidad = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True,db_column='fecha_creacion',null=False)
    sala_id = models.ForeignKey(SalaModel,to_field='id',on_delete=models.CASCADE)

    class Meta:
        db_table='asientos'

