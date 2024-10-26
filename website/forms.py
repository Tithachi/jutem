from django import forms
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['full_name', 'email', 'phone', 'industry', 'company', 'product_enquiry', 'comments']
