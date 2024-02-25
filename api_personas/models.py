from django.db import models


generos = (
    ("M", "Masculino"),
    ("F", "Femenino"),
    ("Otro", "Otro"),
)


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=5, choices=(generos))
    nacionalidad = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f" {self.id} - {self.nombre} - {self.edad} - {self.sexo} - {self.nacionalidad} - {self.profesion} - {self.hobby}"

    class Meta:
        db_table = "tbl_personas"
        ordering = ['-created_at']
