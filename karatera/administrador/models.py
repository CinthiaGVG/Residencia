from django.db import models

# [I] Filtros de clasificacion
class GeneroModel(models.Model):
    Descripcion =  models.CharField(max_length=50, verbose_name="Nombre")
    create = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Actualización")
    class Meta():
        verbose_name = "Genero"
        verbose_name_plural = "Generos"
        ordering = ["-create"]
    def __str__(self):
        return self.Descripcion

class NivelModel(models.Model):
    Descripcion =  models.CharField(max_length=50, verbose_name="Nombre")
    create = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Actualización")
    class Meta():
        verbose_name = "Nivel"
        verbose_name_plural = "Niveles"
        ordering = ["-create"]
    def __str__(self):
        return self.Descripcion

class Cinta_NivelModel(models.Model):
    Descripcion =  models.CharField(max_length=50, verbose_name="Nombre")
    nivelModel = models.ForeignKey(NivelModel, on_delete=models.RESTRICT, verbose_name="Nivel")
    create = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Actualización")
    class Meta():
        verbose_name = "Cinta"
        verbose_name_plural = "Cintas"
        ordering = ["-create"]
    def __str__(self):
        return self.Descripcion

class EdadModel(models.Model):
    Maximo = models.IntegerField(verbose_name="Maximo")
    Minimo = models.IntegerField(verbose_name="Minimo")
    create = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Actualización")
    class Meta():
        verbose_name = "Edad"
        verbose_name_plural = "Edades"
        ordering = ["-Minimo"]    
    def __str__(self):
        return f'({self.Minimo},{self.Maximo})'

class DisciplinaModel(models.Model):
    Descripcion =  models.CharField(max_length=50, verbose_name="Nombre")
    create = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Actualización")
    class Meta():
        verbose_name = "Diciplina"
        verbose_name_plural = "Diciplinas"
        ordering = ["-create"]
    def __str__(self):
        return self.Descripcion 

class ClasificacionKarateModel(models.Model):
    Descripcion =  models.CharField(max_length=50, verbose_name="Nombre")
    nivelModel = models.ForeignKey(NivelModel,verbose_name="Nivel", on_delete=models.RESTRICT)    
    generoModel = models.ForeignKey(GeneroModel,verbose_name="Genero", on_delete=models.RESTRICT)
    edadModel = models.ForeignKey(EdadModel,verbose_name="Edad", on_delete=models.RESTRICT)
    disciplinaModel = models.ForeignKey(DisciplinaModel, verbose_name="Disciplina" , on_delete=models.RESTRICT)
    create = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Actualización")
    class Meta():
        verbose_name = "Clasificación"
        verbose_name_plural = "Clasificaciones"
        ordering = ["-create"]
    def __str__(self):
        return self.Descripcion   
# [F] Filtros de clasificacion

# [I] Dojo
class ModalidadModel(models.Model):
    Descripcion =  models.CharField(max_length=50, verbose_name="Nombre")
    create = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Actualización")
    class Meta():
        verbose_name = "Modalidad"
        verbose_name_plural = "Modalidades"
        ordering = ["-create"]
    def __str__(self):
        return self.Descripcion 
# [F] Dojo


# [I] Torneo 
class AreaModel(models.Model):
    Descripcion =  models.CharField(max_length=50, verbose_name="Nombre Area")
    create = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Actualización")
    class Meta():
        verbose_name = "Area"
        verbose_name_plural = "Areas"
        ordering = ["-create"]
    def __str__(self):
        return self.Descripcion 
# [F] Torneo

# [I] Para saber si es arbitro o juez
class JuezArbitro_TipoModel(models.Model):
    Descripcion =  models.CharField(max_length=50, verbose_name="Perfil")
    create = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Actualización")
    class Meta():
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        ordering = ["-create"]
    def __str__(self):
        return self.Descripcion 
# [F] Torneo

# [I] 
class JuezArbitroModel(models.Model):
    juezArbitro_TipoModel= models.ForeignKey(JuezArbitro_TipoModel,verbose_name="Perfil", on_delete=models.RESTRICT)
    Descripcion =  models.CharField(max_length=50, verbose_name="Nombre")
    create = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Actualización")
    class Meta():
        verbose_name = "Area"
        verbose_name_plural = "Areas"
        ordering = ["-create"]
    def __str__(self):
        return self.Descripcion 
# [F] Torneo

