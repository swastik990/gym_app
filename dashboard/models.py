from django.db import models

class Category(models.Model):
    """
    Represents membership categories (Morning, Evening, Jumba, etc.).
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name