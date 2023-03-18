from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)