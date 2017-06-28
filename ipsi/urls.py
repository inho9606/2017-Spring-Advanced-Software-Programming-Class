from django.conf.urls import url
from . import views
app_name = 'ipsi'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.ipsi_detail, name='ipsi_detail'),
	url(r'^new/$', views.input_data, name='input_data'),
# 	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
# 	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

