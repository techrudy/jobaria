from django.contrib import admin
from .models import Candidate, Professional, Companies

# Register your models here.


admin.site.register([Candidate, Companies, Professional])
admin.site.site_url = "http://cv-buffer.fr"
