from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Gig(models.Model):

	# signups

	UNIFORM_CHOICES = (
		('MV', "Mav'rik"),
		('AT', "Athletics"),
		('FD', "Full Dress"),
	)

	name = models.CharField(max_length=200)
	description = models.TextField()

	uniform = models.CharField(max_length=10,
								choices=UNIFORM_CHOICES,
								default='MV')

	start_datetime = models.DateTimeField()
	end_datetime = models.DateTimeField(blank=True, null=True)
	
	extra_credit = models.BooleanField(default=False)
	cars = models.BooleanField(default=False)

	def __unicode__(self):
		return "{0}".format(self.name)

	def is_past(self):
		return start_datetime < datetime.datetime.now()


class SignUp(models.Model):

	user = models.ForeignKey(User, related_name='signed_up_for')
	gig = models.ForeignKey(Gig, related_name='signups')

	stamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "{0} : {1}".format(self.user, self.gig)