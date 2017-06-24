from django.shortcuts import render
# Create your views here.
from ipsi.models import *
def index(request):
	return render(request, 'ipsi/index.html', {})

def get_data(**user):
	new = Apply(sat_year = user[sat_year], apply_univ = user[apply_univ], apply_faculty = user[apply_faculty], apply_way = user[apply_way], origin_school = user[origin_school])
	new.save()
	if user[jungsi] == 1:
		n = new.jungsi_set.create(sat_kor = user[kor], sat_math = user[math], sat_gpa_eng = user[eng], sat_gpa_history = user[history], sat_choice1 = user[choice1], sat_choice2 = user[choice2], sat_language = user[language])
	else:
		n = new.susi_set.create(gpa = user[gpa], non_subject = user[non_subject], subject = user[subject], interview = user[interview])
	n.save()
