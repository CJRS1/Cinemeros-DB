# Generated by Django 4.1.3 on 2022-12-28 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CineModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('direccion', models.CharField(max_length=50, unique=True)),
                ('cantSalas', models.IntegerField()),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')),
            ],
            options={
                'db_table': 'cines',
            },
        ),
        migrations.CreateModel(
            name='PeliculaModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('peliculas', models.CharField(max_length=50)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')),
            ],
            options={
                'db_table': 'peliculas',
            },
        ),
        migrations.CreateModel(
            name='SalaModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('id_sala', models.CharField(max_length=10, unique=True)),
                ('cantAsientos', models.IntegerField()),
                ('duracion', models.TimeField()),
                ('cine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.cinemodel')),
                ('id_pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.peliculamodel')),
            ],
            options={
                'db_table': 'salas',
            },
        ),
        migrations.CreateModel(
            name='AsientoModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('id_asiento', models.CharField(max_length=2)),
                ('disponibilidad', models.BooleanField(default=True)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')),
                ('sala_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.salamodel')),
            ],
            options={
                'db_table': 'asientos',
            },
        ),
        migrations.CreateModel(
            name='UsuarioModel',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=50, unique=True)),
                ('password', models.TextField()),
                ('tipoUsuario', models.CharField(choices=[('ADMIN', 'ADMINISTRADOS'), ('USER', 'USUARIO')], db_column='tipo_usuario', default='USER', max_length=13)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
    ]
