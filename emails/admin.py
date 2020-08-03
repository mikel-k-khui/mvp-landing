from django.contrib import admin

# Register your models here.
from emails.models import EmailEntry

admin.site.register(EmailEntry)