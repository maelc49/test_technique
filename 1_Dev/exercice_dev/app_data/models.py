from django.db import models

# Create your models here.

class Annonce(models.Model):
    prix = models.IntegerField(blank = True)
    departement = models.IntegerField(blank = True)
    ville = models.CharField(max_length = 200, blank = True)
    code_ville = models.IntegerField(blank = True)
