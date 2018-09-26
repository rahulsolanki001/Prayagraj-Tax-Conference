from django.contrib import admin
from .models import Register

class RegisterAdmin(admin.ModelAdmin):
	fields=('name','profession','city','arrival_date','departure_date','spouse','spouse_profession','arrival','hotel')
	list_display=('name','profession','city','arrival_date','departure_date','spouse','spouse_profession','arrival','hotel')

# Register your models here.


admin.site.register(Register,RegisterAdmin)
