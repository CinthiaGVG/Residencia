from django.db import models
from administrador.models import JuezArbitroModel,AreaModel
# Create your models here.
class TorneoModel(models.Model):
    Descripcion =  models.CharField(max_length=50, verbose_name="Nombre")
    Lugar= models.CharField(max_length=50, verbose_name="Lugar")
    FechaTorneo= models.DateField(verbose_name="Fecha Torneo")
    create = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Actualización")
    class Meta():
        verbose_name = "Modalidad"
        verbose_name_plural = "Modalidades"
        ordering = ["-create"]
    def __str__(self):
        return self.Descripcion 
# [F] Dojo

# [I] Torneo_JuezArbitro
class Torneo_JuezArbitroModel(models.Model):
    juezArbitroModel= models.ForeignKey(JuezArbitroModel, verbose_name="Perfil", on_delete=models.RESTRICT)
    torneoModel= models.ForeignKey(TorneoModel, verbose_name="Torneo", on_delete=models.RESTRICT)
    create = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Actualización")
    def __str__(self):
        return self.create
# [F] Torneo_Area

# [I] Torneo_Area
class Torneo_Area(models.Model):
    torneoModel= models.ForeignKey(TorneoModel, verbose_name="Torneo", on_delete=models.RESTRICT)
    areaModel = models.ForeignKey(AreaModel, verbose_name="Area", on_delete=models.RESTRICT)
    CantidadVoluntarios=models.IntegerField(verbose_name="Cantidad Voluntarios")
    CantidadArea = models.IntegerField(verbose_name="Cantidad de Areas")
    create = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Actualización")
    class Meta():
        verbose_name = "Area"
        verbose_name_plural = "Areas"
        ordering = ["-create"]
    def __str__(self):
        return self.create
# [F] Torneo_Area        