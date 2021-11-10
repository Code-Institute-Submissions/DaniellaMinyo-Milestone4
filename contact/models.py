from django.db import models

# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=200, null=False, blank=False)
    message = models.CharField(
        max_length=5000, null=False, blank=False, default='SOME STRING')

    def __str__(self):
        return self.full_name
