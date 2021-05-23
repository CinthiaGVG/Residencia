from django.db import models
from administrador.models import ClasificacionKarateModel,ModalidadModel
from participante.models import ParticipanteModel

# Create your models here.
class DojoModel(models.Model):
    ##Descripcion = models.CharField(max_length=50,verbose_name="Descripcion")
    NombreDojo = models.CharField(max_length=50, verbose_name="Nombre")
    NombreSensei= models.CharField(max_length=50, verbose_name="Sensei")
    Tel= models.IntegerField(verbose_name="Tel.")
    create = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Actualización")
    def __str__(self):
        return self.NombreDojo  

class EquipoModel(models.Model):
    Descripcion = models.CharField(max_length=50,verbose_name="Nombre del equipo")
    dojoModel = models.ForeignKey(DojoModel, verbose_name="Dojo", on_delete=models.RESTRICT)
    clasificacionModel = models.ForeignKey(ClasificacionKarateModel, verbose_name="Clasificacion", on_delete=models.RESTRICT)
    create = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Actualización")  
    class Meta():
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        ordering = ["-create"]
    def __str__(self):
        return self.Descripcion    

class Participante_ModalidadModel(models.Model):
    modalidadModel=models.ForeignKey(ModalidadModel, verbose_name="Modalidad", on_delete=models.RESTRICT)
    equipoModel=models.ForeignKey(EquipoModel, verbose_name="Equipo", on_delete=models.RESTRICT)
    participanteModel=models.ForeignKey(ParticipanteModel, verbose_name="Participante", on_delete=models.RESTRICT)
    clasificacionModel = models.ForeignKey(ClasificacionKarateModel, verbose_name="Clasificacion", on_delete=models.RESTRICT)
    create = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Actualización")  
    class Meta():
        verbose_name = "Participante"
        verbose_name_plural = "Participantes"
        ordering = ["-create"]
    def __str__(self):
        return self.Descripcion