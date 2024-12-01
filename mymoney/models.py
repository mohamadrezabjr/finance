from django.db import models
from django.contrib.auth.models import User
class expense(models.Model):
    text = models.TextField(null=True, blank=True)
    date = models.DateField()
    amount = models.BigIntegerField()
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
