# Generated by Django 3.2.2 on 2021-05-16 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administrador', '0002_alter_cinta_nivelmodel_nivelmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='DojoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreDojo', models.CharField(max_length=50, verbose_name='Nombre')),
                ('NombreSensei', models.CharField(max_length=50, verbose_name='Sensei')),
                ('Tel', models.IntegerField(verbose_name='Tel.')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Actualización')),
            ],
            options={
                'verbose_name': 'Dojo',
                'verbose_name_plural': 'Dojos',
                'ordering': ['-create'],
            },
        ),
        migrations.CreateModel(
            name='EquipoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=50, verbose_name='Nombre del equipo')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Actualización')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
                'ordering': ['-create'],
            },
        ),
        migrations.CreateModel(
            name='Participante_ModalidadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Actualización')),
                ('clasificacionModel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrador.clasificacionkaratemodel', verbose_name='Clasificacion')),
                ('equipoModel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='dojo.equipomodel', verbose_name='Equipo')),
                ('modalidadModel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrador.modalidadmodel', verbose_name='Modalidad')),
            ],
            options={
                'verbose_name': 'Participante',
                'verbose_name_plural': 'Participantes',
                'ordering': ['-create'],
            },
        ),
    ]
