from django.db.models import * 
from django.contrib.auth.models import User

# Create your models here.
class Profile(Model):
	user = OneToOneField(User, related_name="profile")
	contactNum = IntegerField()

class Car(Model):
	owner = OneToOneField(Profile)
	registeredNumber = CharField(max_length = 10)
	model = CharField(max_length=30, blank=True)
	color = CharField(max_length = 10, blank=True)
	seats = IntegerField(default=1)
	leaveTime = DateTimeField()
	flexible = BooleanField(default=False)
	flexibleTimeLimit = IntegerField(blank=True, null=True, help_text="in minutes")
	def __unicode__(self):
		return self.model

class Seat(Model):
	car = ForeignKey(Car)
	vacant = BooleanField(default = True)
	occupiedBy =  OneToOneField(Profile, null=True, blank = True)
	def __unicode__(self):
		return self.vacant
