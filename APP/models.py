from django.db import models

class checkout(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    mail = models.EmailField()

    def __str__(self):
        return self.username
    



