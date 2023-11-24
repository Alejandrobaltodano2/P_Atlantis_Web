from django.db import models

# Create your models here.
class Platos(models.Model):
    id = models.AutoField(primary_key=True)
    categoria_pltaos=(
                      ('0','Criollos'),
                      ('1','Ceviches'),
                      ('2','Especialidades'),
                      ('3','Chicharrones'),
                      ('4','Parrillas'),
                      ('5','postres'),
                      ('6','Gaseosas'),
                      ('7','TAPERS')
                      )
    
    nombre_plato = models.CharField('nombre_plato',max_length=250)
    categoria = models.CharField('Categoria', max_length=1,choices=categoria_pltaos)

    imagen = models.ImageField(upload_to='platos')
    precio = models.FloatField('precio')

    def __str__(self):
        return str(self.id)+' '+self.nombre_plato