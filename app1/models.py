from django.db import models

class AutoProizvodjac(models.Model):
	
	ime = models.CharField(max_length=50)
	web_stranica = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	logo = models.CharField(max_length=300)

	def __str__(self):
		return self.ime

class AutoModel(models.Model):

	tip = models.CharField(max_length=50)
	verzija=models.IntegerField(null=False)
	godina_proizvodnje = models.DateField(null=True)
	slika = models.CharField(max_length=300)
	automobili = models.ForeignKey(AutoProizvodjac, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.tip