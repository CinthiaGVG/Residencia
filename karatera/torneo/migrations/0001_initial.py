# Generated by Django 3.2.2 on 2021-05-09 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TorneoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=50, verbose_name='Nombre')),
                ('Lugar', models.CharField(max_length=50, verbose_name='Lugar')),
                ('FechaTorneo', models.DateField(verbose_name='Fecha Torneo')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Actualización')),
            ],
            options={
                'verbose_name': 'Modalidad',
                'verbose_name_plural': 'Modalidades',
                'ordering': ['-create'],
            },
        ),
        migrations.CreateModel(
            name='Torneo_JuezArbitroModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Actualización')),
                ('juezArbitroModel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrador.juezarbitromodel', verbose_name='Perfil')),
                ('torneoModel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='torneo.torneomodel', verbose_name='Torneo')),
            ],
        ),
        migrations.CreateModel(
            name='Torneo_Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CantidadVoluntarios', models.IntegerField(verbose_name='Cantidad Voluntarios')),
                ('CantidadArea', models.IntegerField(verbose_name='Cantidad de Areas')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Actualización')),
                ('areaModel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrador.areamodel', verbose_name='Area')),
                ('torneoModel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='torneo.torneomodel', verbose_name='Torneo')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
                'ordering': ['-create'],
            },
        ),
    ]
