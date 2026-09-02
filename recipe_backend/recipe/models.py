from django.db import models
from datetime import datetime

# Create your models here.

class Recipe:
	def __init__(self, name, color, created=None):
		self.name = name
		self.color = color
		self.created = datetime.now()

recipe = Recipe(name = 'default recipe', color = 'nothing')
