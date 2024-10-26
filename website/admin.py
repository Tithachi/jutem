from django.contrib import admin
from .models import Enquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'industry', 'company', 'product_enquiry', 'comments')
    list_filter = ('industry', 'product_enquiry')
    search_fields = ('full_name', 'email', 'phone')

    # Optional: You can customize the form layout if needed
    fieldsets = (
        (None, {
            'fields': ('full_name', 'email', 'phone', 'industry', 'company', 'product_enquiry', 'comments')
        }),
    )


