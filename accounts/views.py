# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login as auth_login
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from .forms import SignUpForm, UserForm, ProfileForm
from .models import StProfile

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'students/signup.html', {'form': form})

#@method_decorator(login_required, name='dispatch')
#class UserUpdateView(UpdateView):
#    model = User
#    fields = ('first_name', 'last_name', 'email','username')
#    template_name = 'students/my_account.html'
#    success_url = reverse_lazy('my_account')
#    def get_object(self):
#        return self.request.user

def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.stprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

        return HttpResponseRedirect(reverse('home'))
            #render(request, 'students/my_account.html',{'user_form': user_form, 'profile_form': profile_form})
    else:
        user_id = User.objects.get(pk= request.user.pk)
        user_form = UserForm(instance= request.user)
        user_id.stprofile, created = StProfile.objects.get_or_create(user=user_id)
        profile_form = ProfileForm(instance= request.user.stprofile)
        return render(request, 'students/my_account.html',{'user_form': user_form, 'profile_form': profile_form} )