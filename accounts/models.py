from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    cumpleaños = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"