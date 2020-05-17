from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
	"""docstring for User"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	site_web = models.URLField(blank=True)
	signature = models.TextField(blank = True)
	inscrit_newsletter = models.BooleanField(default=False)
	def __str__(self):
		return "User de {0}".format(self.user.username)

class Species(models.Model):
		speciesName = models.CharField(max_length=1000)
		moleculeName = models.CharField(max_length = 1000)
		publishedDate = models.DateTimeField( default=timezone.now)
		
		def __str__(self):
			return self.speciesName
	

