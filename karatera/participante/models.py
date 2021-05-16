from django.db import models
from administrador.models import NivelModel,ClasificacionKarateModel,ModalidadModel,GeneroModel

# Create your models here.
class ParticipanteModel(models.Model):    
    Nombre = models.CharField(max_length=50, verbose_name="Nombre")
    NumParticipante = models.IntegerField(verbose_name="NumParticipante")
    FechaNacimiento= models.DateField(verbose_name="Fecha Nacimiento")
    Edad = models.IntegerField(verbose_name="Edad")
    generoModel = models.ForeignKey(GeneroModel,verbose_name="Genero", on_delete=models.RESTRICT)
    Peso = models.IntegerField(verbose_name="Peso")
    dojoModel=models.ForeignKey("dojo.DojoModel", verbose_name="Dojo", on_delete=models.RESTRICT)  
    # Nivel Usuario
    nivelKata = models.ForeignKey(NivelModel, verbose_name="NivelKata", on_delete=models.RESTRICT, related_name="nivelKata")
    nivelKumite= models.ForeignKey(NivelModel, verbose_name="NivelKumite", on_delete=models.RESTRICT, related_name="nivelKumite")
    # Clasificacion Sistema
    clasificacionKata = models.ForeignKey(ClasificacionKarateModel,verbose_name="NivelKata", on_delete=models.RESTRICT, related_name="clasificacionKata")    
    clasificacionKumite= models.ForeignKey(ClasificacionKarateModel,verbose_name="NivelKumite", on_delete=models.RESTRICT,related_name="clasificacionKumite") 
    # Modalidad
  # modalidadKata = models.ForeignKey(ModalidadModel,verbose_name="NivelKata", on_delete=models.RESTRICT)    
  # modalidadKumite= models.ForeignKey(ModalidadModel,verbose_name="NivelKumite", on_delete=models.RESTRICT) 

    create = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Actualización")    
    class Meta():
        verbose_name = "Dojo"
        verbose_name_plural = "Dojos"
        ordering = ["-create"]
    def __str__(self):
        return self.Nombre