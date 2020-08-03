from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
from .forms import EmailEntryForm
from .models import EmailEntry

# CRUD
def email_entry_get(request, id=None, *args, **kwargs):

  try:
    obj = EmailEntry.objects.get(id=id)
  except EmailEntry.DoesNotExist: # specific DB error
    raise Http404
  return render(request, 'get.html', {'object': obj, 'id': id})

def email_entry_get_list():

  return

def email_entry_create_view(request, *args, **kwargs):
  form = EmailEntryForm(request.POST or None)

  if form.is_valid():
    '''
    # no data check
    form.save()
    '''
    # check data if needed
    obj = form.save(commit=False) # Model instance
    obj.save()
    new_id = obj.id
    form = EmailEntryForm()
    return HttpResponseRedirect(f"/email/{new_id}")
  return render(request, 'form.html', {'form': form})

def email_entry_update_view():

  return

def email_entry_delete_view():

  return