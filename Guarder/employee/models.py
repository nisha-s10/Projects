from django.db import models
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
class Employee(models.Model):
    employee_id = models.CharField(max_length=10, primary_key=True)  # Use employee ID as primary key
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords
    # Add other relevant fields
    name = models.CharField(max_length=100)  # Example field for employee name
    dob = models.DateField()
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.employee_id})"  # Display name and ID in admin

    def save(self, *args, **kwargs):
        # Generate a URL that redirects to the employee's details page
        qr_data = f"https://yourdomain.com/details/{self.employee_id}/"

        # Generate QR Code
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save image to a BytesIO buffer
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # Save image to the ImageField
        self.qr_code.save(f"{self.employee_id}_qr.png", ContentFile(buffer.read()), save=False)

        super().save(*args, **kwargs)