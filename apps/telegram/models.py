from django.db import models

# Create your models here.


class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(max_length=255, verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return f"Review by {self.name} on {self.created_at}"
