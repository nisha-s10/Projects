from django.db import models

class Owner(models.Model):
    owner_id = models.CharField(max_length=10, primary_key=True)  # Use owner ID as primary key
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords
    # Add other relevant fields
    name = models.CharField(max_length=100)  # Example field for owner name

    def __str__(self):
        return f"{self.name} ({self.owner_id})"  # Display name and ID in admin
