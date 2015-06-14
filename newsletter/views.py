from django.conf import settings #allow to use settings value
from django.shortcuts import render
from django.core.mail import send_mail

from .forms import SignUpForm, ContactForm

# Create your views here.
def home(request):
    title = "Welcome"
    #if request.user.is_authenticated():
        #title = "Your name is %s" %(request.user)

    #add a form
    if request.method == "POST":
        print request.POST
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }
    if form.is_valid():
    	#print request.POST['email'] #not recommended
    	ins = form.save(commit=False)

    	full_name = form.cleaned_data.get("full_name")
    	if not full_name:
    		full_name = "New User"
        ins.full_name = full_name
    	ins.save()
    	print ins.email
    	print ins.full_name
    	print ins.timestamp
    	context = {
    	    "title": "Thank you"
    	}

    return render(request, "home.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    title = "Contact Us"
    if form.is_valid():
    	#print form.cleaned_data
    	form_email = form.cleaned_data.get("email")
    	form_message = form.cleaned_data.get("message")
    	form_full_name = form.cleaned_data.get("full_name")
    	subject = 'Site contact form'
    	from_email = settings.EMAIL_HOST_USER
    	to_email = [from_email, 'rubyinhell@gmail.com']
    	contact_message = "%s: %s via %s"%(form_full_name, form_message, form_email)

    	send_mail(subject,
    	         contact_message,
    	         form_email,
    	         to_email,
    	         fail_silently=True)
    context = {
        "form": form,
        "title": title,
    }
    return render(request, "forms.html", context)