from django.db import models

class FutsalField(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=255)
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    open_time = models.TimeField(default="07:00")
    close_time = models.TimeField(default="00:00")
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.location}"
