from django.db import models

# Create your models here.
from django.db import models

class Enquiry(models.Model):
    INDUSTRY_CHOICES = [
        ('Agriculture', 'Agriculture'),
        ('Construction', 'Construction'),
        ('Education', 'Education'),
        ('Healthcare', 'Healthcare'),
        ('Information Technology', 'Information Technology'),
        ('Manufacturing', 'Manufacturing'),
        ('Retail', 'Retail'),
        ('Telecommunications', 'Telecommunications'),
        ('Transportation', 'Transportation'),
        ('Other', 'Other'),
    ]
    
    PRODUCT_CHOICES = [
        ('Funding and Advisory Services', 'Funding and Advisory Services'),
        ('Micro Financing', 'Micro Financing'),
        ('Product Financing', 'Product Financing'),
        ('Business Strategy Advisory', 'Business Strategy Advisory'),
    ]

    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)  # Adjust length based on expected phone number format
    industry = models.CharField(max_length=30, choices=INDUSTRY_CHOICES, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    product_enquiry = models.CharField(max_length=30, choices=PRODUCT_CHOICES, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.full_name

