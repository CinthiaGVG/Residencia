# Generated by Django 3.2.2 on 2021-05-09 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=50, verbose_name='Nombre Area')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Actualización')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
                'ordering': ['-create'],
            },
        ),
        migrations.CreateModel(
            name='DisciplinaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=50, verbose_name='Nombre')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Actualización')),
            ],
            options={
                'verbose_name': 'Diciplina',
                'verbose_name_plural': 'Diciplinas',
                'ordering': ['-create'],
            },
        ),
        migrations.CreateModel(
            name='EdadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Maximo', models.IntegerField(verbose_name='Maximo')),
                ('Minimo', models.IntegerField(verbose_name='Minimo')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Actualización')),
            ],
            options={
                'verbose_name': 'Edad',
                'verbose_name_plural': 'Edades',
                'ordering': ['-create'],
            },
        ),
        migrations.CreateModel(
            name='GeneroModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=50, verbose_name='Nombre')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Actualización')),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
                'ordering': ['-create'],
            },
        ),
        migrations.CreateModel(
            name='JuezArbitro_TipoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=50, verbose_name='Perfil')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Actualización')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
                'ordering': ['-create'],
            },
        ),
        migrations.CreateModel(
            name='ModalidadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=50, verbose_name='Nombre')),
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
            name='NivelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=50, verbose_name='Nombre')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Actualización')),
            ],
            options={
                'verbose_name': 'Nivel',
                'verbose_name_plural': 'Niveles',
                'ordering': ['-create'],
            },
        ),
        migrations.CreateModel(
            name='JuezArbitroModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=50, verbose_name='Nombre')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Actualización')),
                ('juezArbitro_TipoModel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrador.juezarbitro_tipomodel', verbose_name='Perfil')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
                'ordering': ['-create'],
            },
        ),
        migrations.CreateModel(
            name='ClasificacionKarateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=50, verbose_name='Nombre')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Actualización')),
                ('disciplinaModel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrador.disciplinamodel', verbose_name='Disciplina')),
                ('edadModel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrador.edadmodel', verbose_name='Edad')),
                ('generoModel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrador.generomodel', verbose_name='Genero')),
                ('nivelModel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrador.nivelmodel', verbose_name='Nivel')),
            ],
            options={
                'verbose_name': 'Clasificación',
                'verbose_name_plural': 'Clasificaciones',
                'ordering': ['-create'],
            },
        ),
        migrations.CreateModel(
            name='Cinta_NivelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=50, verbose_name='Nombre')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Actualización')),
                ('nivelModel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrador.nivelmodel')),
            ],
            options={
                'verbose_name': 'Cinta',
                'verbose_name_plural': 'Cintas',
                'ordering': ['-create'],
            },
        ),
    ]
