from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Bar, Drink
from forms import BarForm, DrinkForm
from views import BarCreate, DrinkCreate, BarDetail, review, signup

urlpatterns = [

# List latest Bars/
    url(r'home',
        ListView.as_view(
        	queryset=Bar.objects.all(),
        	context_object_name='latest_bar_list',
        	template_name='hotbarslocal/bar_list.html'),
        name='bar_list'),

# Restaurant details, ex.: /myrestaurants/restaurants/1/
    url(r'^bar/(?P<pk>\d+)/$',
        BarDetail.as_view(),
        name='bar_detail'),

# Restaurant dish details, ex: /myrestaurants/restaurants/1/dishes/1/
    url(r'^bars/(?P<pkr>\d+)/drinks/(?P<pk>\d+)/$',
        DetailView.as_view(
        	model=Drink,
        	template_name='hotbarslocal/drink_detail.html'),
        name='drink_detail'),

# Create a restaurant, /myrestaurants/restaurants/create/
    url(r'^bars/create/$',
        BarCreate.as_view(),
        name='bar_create'),

# Edit restaurant details, ex.: /myrestaurants/restaurants/1/edit/
    url(r'^bars/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
        	model = Bar,
        	template_name = 'hotbarslocal/form.html',
        	form_class = BarForm),
        name='bar_edit'),

# Create a restaurant dish, ex.: /myrestaurants/restaurants/1/dishes/create/
    url(r'^bars/(?P<pk>\d+)/drinks/create/$',
    	DrinkCreate.as_view(),
        name='drink_create'),

# Edit restaurant dish details, ex.: /myrestaurants/restaurants/1/dishes/1/edit/
    url(r'^bars/(?P<pkr>\d+)/drinks/(?P<pk>\\d+)/edit/$',
    	UpdateView.as_view(
    		model = Drink,
    		template_name = 'hotelbarslocal/form.html',
    		form_class = DrinkForm),
    	name='drink_edit'),



    url(r'^restaurants/(?P<pk>\d+)/reviews/create/$',
        review,
        name='review_create'),
#URL for Signup PAGE VIEW
    url(r'^signup/$', signup, name='signup'),
]
