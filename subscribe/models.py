from django.db import models

# Create your models here.


class Subscribe(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.email
