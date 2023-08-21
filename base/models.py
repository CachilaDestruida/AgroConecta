from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Producto(models.Model):
    title =  models.CharField(max_length = 255, blank=True, null=True)
    content = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    imagen = models.ImageField(upload_to='static/images/productos/', null=True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    user =  models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    updated = models.DateTimeField (auto_now=True)
    created = models.DateTimeField (auto_now_add=True)
    