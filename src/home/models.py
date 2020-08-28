from django.db import models

class Slider(models.Model):
	title = models.CharField(max_length=200, blank=False)
	sub_title = models.CharField(max_length=200, blank=False)
	sub_sub_title = models.CharField(max_length=200, blank=True)
	short_text = models.CharField(max_length=200, blank=True)
	image = models.ImageField(upload_to='media/homeslider', blank=False)

	class Meta:
		verbose_name = 'Slider'
		verbose_name_plural = 'Sliders'	

	def __str__(self):
		return self.title

