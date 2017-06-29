from django.shortcuts import get_object_or_404, render, redirect
# Create your views here.
from ipsi.models import *
from ipsi.forms import ApplyForm, JungsiForm, SusiForm

def index(request):
	datas = Apply.objects.order_by('-pk')
	return render(request, 'ipsi/index.html', {'datas': datas})

def ipsi_detail(request, pk):
	data = get_object_or_404(Apply, pk=pk)
	return render(request, 'ipsi/detail.html', {'data': data})

def search_rank(my_data):
	data_list = Apply.objects.filter(sat_year= my_data.sat_year).filter(apply_univ = my_data.apply_univ).filter(apply_faculty = my_data.apply_faculty).filter(apply_way = my_data.apply_way).filter(options = my_data.options)
	rank = 1
	if my_data.options == 'j':
		temp = my_data.jungsi_set.first()
		my_sum = temp.sat_kor + temp.sat_math + temp.sat_choice1 + temp.sat_choice2
		for data in data_list:
			if data.pk == my_data.pk: continue
			temp = data.jungsi_set.first()
			temp_sum = temp.sat_kor + temp.sat_math + temp.sat_choice1 + temp.sat_choice2
			if temp_sum > my_sum: rank += 1
		return rank, len(data_list)
	if my_data.options == 's':
		temp = my_data.susi_set.first()
		my_gpa = temp.gpa
		for data in data_list:
			if data.pk == my_data.pk: continue
			temp = data.susi_set.first()
			temp.gpa = temp.gpa
			if my_gpa > temp.gpa: rank += 1
		return rank, len(data_list)

def output_data(request, my_data):
	my_rank, total = search_rank(my_data)
	return render(request, 'ipsi/ipsi_result.html', {'rank': my_rank, 'data': my_data, 'total': total})

"""
def input_data(request):
	if request.method == "POST":
		form = ApplyForm(request.POST)
		if form.is_valid():
			data = form.save()
			request.method = "GET"
			final_data = JungsiForm()
			return render(request, 'ipsi/ipsi_add.html', {'form': final_data})
		else:
			form = JungsiForm(request.POST)
			if form.is_valid():
				obj = form.save(commit=False)
				obj.apply = Apply.objects.order_by('-pk')[0]
				obj.save()
				return output_data(request, obj.apply)
	else:
		data = ApplyForm()
		return render(request, 'ipsi/ipsi_add.html', {'form': data})
"""

def input_data(request):
	if request.method == "POST":
		form = ApplyForm(request.POST)
		if form.is_valid():
			data = form.save()
			request.method = "GET"
			if data.options == 's': final_data = SusiForm()
			elif data.options == 'j': final_data = JungsiForm()
			return render(request, 'ipsi/ipsi_add.html', {'form': final_data})
		else:
			if Apply.objects.order_by('-pk')[0].options == 's': form = SusiForm(request.POST)
			elif Apply.objects.order_by('-pk')[0].options == 'j': form = JungsiForm(request.POST)
			if form.is_valid():
				obj = form.save(commit=False)
				obj.apply = Apply.objects.order_by('-pk')[0]
				obj.save()
				return output_data(request, obj.apply)
	else:
		data = ApplyForm()
		return render(request, 'ipsi/ipsi_add.html', {'form': data})
