from django.db import models

class Ciudad(models.Model):

    ciudad = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Ciudad'
        verbose_name_plural='Ciudades'
    def __str__(self):
        return self.ciudad


class Categoria(models.Model):

    dato = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
    def __str__(self):
        return self.dato

class Beneficiario(models.Model):

    persona = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
  
    class Meta:
        verbose_name='Beneficiario'
        verbose_name_plural='Beneficiarios'
    def __str__(self):
        return self.persona


class Donacion(models.Model):

    nombre = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ciudad =  models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    persona = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    correo = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Donacion'
        verbose_name_plural='Donaciones'
    def __str__(self):
        return self.nombre



