from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Vendedor (models.Model):
    id_vendedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('vendedor_edit', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'vendedor'


class Operacion (models.Model):
    id_operacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('vendedor_edit', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'operacion'


class Provincia (models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('vendedor_edit', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'provincia'


class TipoInmueble (models.Model):
    id_tipo_inmueble = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('vendedor_edit', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'tipo_inmueble'


class Inmueble (models.Model):
    id_inmueble = models.AutoField(primary_key=True)
    fecha_alta = models.DateTimeField(auto_now_add=True)
    id_tipo = models.ForeignKey(TipoInmueble, db_column='id_tipo',
                                on_delete=models.CASCADE)
    id_operacion = models.ForeignKey(Operacion,
                                     db_column='id_operacion', on_delete=models.CASCADE)
    id_provincia = models.ForeignKey(Provincia,
                                     db_column='id_provincia', on_delete=models.CASCADE)
    superficie = models.FloatField(validators=[MinValueValidator(0.00),
                                               MaxValueValidator(9999.99)])
    precio_venta = models.FloatField(validators=[MinValueValidator(0.00),
                                                 MaxValueValidator(99999999.99)])
    fecha_venta = models.DateTimeField(null=True, blank=True)
    id_vendedor = models.ForeignKey(
        Vendedor, db_column='id_vendedor', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_inmueble)

    def get_absolute_url(self):
        return reverse('vendedor_edit', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'inmueble'
