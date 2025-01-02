from django.db import models
from django.contrib.auth.models import User

class expense(models.Model):
    text = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user} - {self.text}  in : {self.date}"

class income(models.Model):
    text = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user} - {self.text}  in : {self.date}"
