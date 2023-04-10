from django.db import models


class Input(models.Model):
    image = models.FileField(upload_to='images/')
    text = models.CharField(max_length=5000)

    def __str__(self):
        return self.text