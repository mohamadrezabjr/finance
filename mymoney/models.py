from django.db import models
from django.contrib.auth.models import User

class Token (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    def __str__(self):
        return "{}'s Token".format(self.user)

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
