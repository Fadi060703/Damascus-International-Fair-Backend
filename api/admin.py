from django.contrib import admin
from .models import * 

# Register your models here.

admin.site.register( Coordinates ) 
admin.site.register( Article ) 
admin.site.register( CompanyBusField ) 
admin.site.register( ParticipantCompany ) 
admin.site.register( Offer ) 