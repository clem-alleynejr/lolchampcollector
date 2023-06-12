from django.db import models

class LolChamp(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)

    def __str__(self):
        return self.name




