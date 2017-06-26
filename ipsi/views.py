from django.shortcuts import get_object_or_404, render, redirect
# Create your views here.
from ipsi.models import *

def index(request):
	datas = Apply.objects.order_by('-pk')
	return render(request, 'ipsi/index.html', {'datas': datas})

def ipsi_detail(request, pk):
	data = get_object_or_404(Apply, pk=pk)
	return render(request, 'ipsi/detail.html', {'data': data})

def get_data(**user):
	new = Apply.objects.create(sat_year = user[sat_year], apply_univ = user[apply_univ], apply_faculty = user[apply_faculty], apply_way = user[apply_way], origin_school = user[origin_school])
	if user[jungsi] == 1:
		new.jungsi_set.create(sat_kor = user[kor], sat_math = user[math], sat_gpa_eng = user[eng], sat_gpa_history = user[history], sat_choice1 = user[choice1], sat_choice2 = user[choice2], sat_language = user[language])
	else:
		new.susi_set.create(gpa = user[gpa], non_subject = user[non_subject], subject = user[subject], interview = user[interview])

def input_data(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			data = form.save()
			return redirect('ipsi_detail', pk=data.pk)
	else:
		data = PostForm()
		return render(request, 'ipsi/ipsi_add.html', {'data': data})
