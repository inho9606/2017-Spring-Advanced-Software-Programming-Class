from django.db import models

# Create your models here.

class Apply(models.Model):
	sat_year = models.IntegerField()
	apply_univ = models.CharField(max_length=20)
	apply_faculty = models.CharField(max_length=20)
	apply_way = models.CharField(max_length=20)
	origin_school = models.CharField(max_length=30)
	period = (('s', '수시'), ('j', '정시'),)
	options = models.CharField(max_length=1, choices=period, default='정시')
	def __str__(self): # __unicode__ on Python 2
		return self.sat_year

class Susi(models.Model):
	apply = models.ForeignKey(Apply, on_delete=models.CASCADE) 
	gpa = models.FloatField()
	non_subject = models.TextField()
	subject = models.TextField()
	interview = models.TextField()
	status = (('p', 'Progress'), ('r', 'Rejected'), ('a', 'Accepted'))
	result = models.CharField(max_length=1, choices=status, default='Progress')

class Jungsi(models.Model):
	apply = models.ForeignKey(Apply, on_delete=models.CASCADE)
	sat_kor = models.IntegerField()
	sat_math = models.IntegerField()
	sat_gpa_eng = models.IntegerField()
	sat_gpa_history = models.IntegerField()
	sat_choice1 = models.IntegerField()
	sat_choice2 = models.IntegerField()
	sat_language = models.IntegerField()
