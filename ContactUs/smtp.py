from django.core.mail import send_mail
from django.conf import settings
from .models import ContactUs

def SendMail(form):


   
    subject = "Confirmation - We've Received Your Message"

    body = f"""
Subject: Confirmation - We've Received Your Message

Dear {form['name']},

Thank you for reaching out to us through our website! We have received your message and appreciate your interest
in working with us. 

Our team will review the details you provided, and we will get back to you as soon as possible. If we have any additional questions or need more information, we will reach out to you for further clarification.

In the meantime, if you have any urgent inquiries or if you'd like to discuss your project in more detail, please don't hesitate to contact us directly at +91 9113196913.

Thank you once again for considering us for your project. We look forward to the opportunity of working with you.

Best regards,

piyush kumar
+91 9113196913
"""
    

    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [form['email']],  # Convert the recipient's email to a list or tuple
        fail_silently=False,
    )