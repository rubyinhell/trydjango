from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "update"]
    form = SignUpForm
    #class Meta:
        #form = SignUpForm
        #model = SignUp

admin.site.register(SignUp, SignUpAdmin)
