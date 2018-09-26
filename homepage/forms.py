from .models import Register
from django.forms import ModelForm
class Registerform(ModelForm):
	class Meta:
		model=Register
		fields=['name','profession','city','arrival','arrival_date','departure','departure_date','hotel','spouse_check','spouse','spouse_profession']