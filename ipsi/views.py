from django.shortcuts import get_object_or_404, render, redirect
# Create your views here.
from ipsi.models import *

def index(request):
	datas = Apply.objects.order_by('-pk')
	return render(request, 'ipsi/index.html', {'datas': datas})

def ipsi_detail(request, pk):
	data = get_object_or_404(Apply, pk=pk)
	return render(request, 'ipsi/detail.html', {'data': data})

def search_rank(my_data):
	data_list = Apply.objects.filter(sat_year= my_data.sat_year).filter(apply_univ = my_data.apply_univ).filter(apply_faculty = my_data.apply_faculty).filter(apply_way = my_data.apply_way)
	rank = 1
	temp = my_data.jungsi_set.first()
	my_sum = temp.sat_kor + temp.sat_math + temp.sat_choice1 + temp.sat_choice2
	for data in data_list:
		if data.pk == my_data.pk: continue
		temp = data.jungsi_set.first()
		temp_sum = temp.sat_kor + temp.sat_math + temp.sat_choice1 + temp.sat_choice2
		if temp_sum > my_sum: rank += 1
	return rank

def get_data(**user):
	new = Apply.objects.create(sat_year = user['sat_year'], apply_univ = user['apply_univ'], apply_faculty = user['apply_faculty'], apply_way = user['apply_way'], origin_school = user['origin_school'])
	if user['jungsi'] == 1:
		new.jungsi_set.create(sat_kor = user['kor'], sat_math = user['math'], sat_gpa_eng = user['eng'], sat_gpa_history = user['history'], sat_choice1 = user['choice1'], sat_choice2 = user['choice2'], sat_language = user['language'])
	else:
		new.susi_set.create(gpa = user['gpa'], non_subject = user['non_subject'], subject = user['subject'], interview = user['interview'])

def input_data(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			data = form.save()
			return redirect('ipsi_detail', pk=data.pk)
	else:
		data = PostForm()
		return render(request, 'ipsi/ipsi_add.html', {'data': data})

def output_data(request, my_data):
	my_rank = search_rank(my_data)
	return render(request, 'ipsi/ipsi_result.html', {'rank': my_rank, 'data': my_data})
