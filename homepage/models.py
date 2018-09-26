from django.db import models

# Create your models here.
arrival_choice=[('1','Train'),('2','Flight'),('3','Bus'),('4','Own Vehicle')]

class Register(models.Model):
	name=models.CharField(blank=False,verbose_name='Name',max_length=30)
	profession=models.CharField(blank=False,verbose_name='Profession',max_length=20)
	city=models.CharField(blank=False,verbose_name='City',max_length=20)
	arrival=models.CharField(choices=arrival_choice,max_length=20,verbose_name='Mode of Arrival',blank=False)
	arrival_date=models.DateTimeField(auto_now=False,verbose_name='Arrival Date & Time',blank=False)
	departure=models.CharField(choices=arrival_choice,max_length=20,verbose_name='Mode of Departure',blank=False)
	departure_date=models.DateTimeField(auto_now=False,blank=False,verbose_name='Departure Date & Time')
	hotel=models.CharField(blank=False,verbose_name='Name of hotel',max_length=30)
	spouse_check=models.BooleanField(blank=False,verbose_name='Is your spouse coming')
	spouse=models.CharField(verbose_name='Name of spouse',max_length=30)
	spouse_profession=models.CharField(verbose_name='Profession of spouse',max_length=20)

	def __str__(self):
		return str(self.name)



