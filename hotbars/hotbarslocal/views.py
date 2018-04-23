# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from models import BarReview, Bar, Drink
from forms import BarForm, DrinkForm
#Decorator for Login only only lets users that are logged in to see
from django.contrib.auth.decorators import login_required

class BarDetail(DetailView):
    model = Bar
    template_name = 'hotbarslocal/bar_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BarDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = BarReview.RATING_CHOICES
        return context


class BarCreate(CreateView):
    model = Bar
    template_name = 'hotbarslocal/form.html'
    form_class = BarForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BarCreate, self).form_valid(form)


class DrinkCreate(CreateView):
    model = Drink
    template_name = 'hotbarslocal/form.html'
    form_class = DrinkForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.bar = Bar.objects.get(id=self.kwargs['pk'])
        return super(DrinkCreate, self).form_valid(form)




@login_required
def review(request, pk):
    bar = get_object_or_404(Bar, pk=pk)
    if BarReview.objects.filter(bar=bar, user=request.user).exists():
        BarReview.objects.get(bar=bar, user=request.user).delete()
    new_review = BarReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        bar=bar)
    new_review.save()
    return HttpResponseRedirect(reverse('hotbarslocal:bar_detail', args=(bar.id,)))

#Signup VIEW for New USers
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username', False)
            raw_password = form.cleaned_data.get('password1', False)
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'hotbarslocal/signup.html', {'form': form})