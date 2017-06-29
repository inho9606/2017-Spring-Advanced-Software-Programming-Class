from django import forms
from ipsi.models import *
class ApplyForm(forms.ModelForm):
	class Meta:
		model = Apply
		fields = ['sat_year', 'apply_univ', 'apply_faculty', 'apply_way', 'origin_school', 'options']

class JungsiForm(forms.ModelForm):
	class Meta:
		model = Jungsi
		fields = ['sat_kor', 'sat_math', 'sat_gpa_eng', 'sat_gpa_history', 'sat_choice1', 'sat_choice2', 'sat_language',]

class SusiForm(forms.ModelForm):
	class Meta:
		model = Susi
		fields = ['gpa', 'non_subject', 'subject', 'interview', 'result',]