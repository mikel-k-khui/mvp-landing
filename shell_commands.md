## Common Shell Commands

### Django Shell
```python
python manage.py shell
```

### Django Settings

__Accessing global variables/config in `settings.py`__
```python
from django.conf import settings

API_KEY = getattr(settings, 'API_KEY', None)
BASE_DIR = settings.BASE_DIR

```

### Debug
```python
DEBUG = settings.DEBUG
```

### Import of a model
```python
from <appname>.modesl import <ClassName>
e.g. from emails.models import EmailEntry
```

### Query stored item
```python
<ClassName>.objects.get(<criterium>)
e.g. EmailEntry.objects.get(email='tony.stark@marvel.com')
```

```python
<ClassName>.objects.all()
<ClassName>.objects.filter(email='*@marvel.com')
```

### CRUD objects
```python
<ClassName>.objects.create(...)
#or
obj = <ClassName>()
obj.<field> = data
```

```python
obj = <ClassName>.objects.get(...)
obj.<field> = newData
obj.save()
```

```python
obj = <ClassName>.objects.get(...)
obj.delete()
```