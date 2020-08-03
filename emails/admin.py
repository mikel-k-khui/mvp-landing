from django.contrib import admin

# TODO: Register your models here.
from emails.models import EmailEntry

admin.site.register(EmailEntry)