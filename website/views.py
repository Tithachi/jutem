from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Enquiry
from .forms import EnquiryForm  # Ensure you import your form

def index(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            enquiry = form.save()

            # Prepare email
            subject = 'New Enquiry from {}'.format(enquiry.full_name)
            message = (
                f"Full Name: {enquiry.full_name}\n"
                f"Email: {enquiry.email}\n"
                f"Phone: {enquiry.phone}\n"
                f"Industry: {enquiry.industry}\n"
                f"Company: {enquiry.company}\n"
                f"Product Enquiry: {enquiry.product_enquiry}\n"
                f"Comments: {enquiry.comments}"
            )
            from_email = 'info@datoscw.com'  # Replace with your email
            recipient_list = ['timothy.chimfwembe@datoscw.com','mwiya.mwiya@datoscw.com','mwiya108@gmail.com','thapelochimfwembe@gmail.com']  # Replace with recipient email

            # Send email
            send_mail(subject, message, from_email, recipient_list)

            # Redirect or render success page
            return redirect('index')  # Redirect to a success page or back to the form
    else:
        form = EnquiryForm()

    return render(request, 'index.html', {'form': form})
