from django.shortcuts import render
from .models import ContactUs
from django.http import  JsonResponse
from .smtp import SendMail

def contact_us(request):
    contact_form_status_msg = None
    data={}
    if request.method == 'POST':
        
        try:
            #  form processing logic here
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            data['name'] = name
            data['email'] = email
            data['message'] = message
          

            # Validate form data 

            # Save form data to the database
            ContactUs.objects.create(full_name=name, email=email, message=message)
           


            # Set success message
            data['contact_form_status_msg'] = "Form submitted successfully"
            
            SendMail(data)
      
        except Exception as e:
            # Log the error or handle it as appropriate
            print(e)
            data['contact_form_status_msg'] = "An error occurred while processing the form"
            return JsonResponse(data=data)
            # You might also consider returning an error page instead of redirecting

    return render(request=request,template_name='contact-form.html',context=data)
