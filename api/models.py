from django.db import models
from django.utils import timezone
class Retreat(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="")
    date = models.DateField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=255, default="General")  # Added default value
    condition = models.CharField(max_length=255, default="Default Condition")  # Corrected default value
    image = models.URLField(default="")
    tag = models.JSONField(default=list)  # Use a callable for the default
    duration = models.IntegerField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=20)
    retreat = models.ForeignKey(Retreat, on_delete=models.CASCADE)
    payment_details = models.TextField()
    booking_date = models.DateField()

    class Meta:
        unique_together = ('user_id', 'retreat')

    def __str__(self):
        return f'Booking for {self.user_name} on {self.booking_date}'
