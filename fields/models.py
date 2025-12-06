from django.db import models

class FutsalField(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
