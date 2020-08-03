# TODO build custom form

from django import forms

# import model
from .models import EmailEntry

class EmailEntryForm(forms.ModelForm):
  class Meta:
    model = EmailEntry
    fields = ['name', 'email', 'bio', 'consent']

  # TODO: validation specific to emails clean_<field>
  def clean_email(self): 
    email =  self.cleaned_data.get('email')
    # check if email exists
    query = EmailEntry.objects.filter(
      email__iexact=email
    )
    if query.exists():
      raise forms.ValidationError('Thank you, you have already registered')
    return email