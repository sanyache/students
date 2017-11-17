# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from ..models import Group

def groups_list(request):
    groups = Group.objects.all()
    return render(request, 'students/groups_list.html', {'groups': groups})

class GroupCreateView(CreateView):
    model = Group
    template_name = 'students/groups_add.html'
    fields = '__all__'
    def get_success_url(self):
        messages.info(self.request, u"Група успішно добавлена")
        return reverse('groups')
    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel'):
            messages.warning(self.request, u"Сторення групи відмінено")
            return HttpResponseRedirect(reverse('groups'))
        else:
            return super(GroupCreateView, self).post(request, *args, **kwargs)

class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'students/groups_edit.html'
    fields = '__all__'

    def get_success_url(self):
        messages.info(self.request, u"Групу успішно збережено")
        return reverse('groups')
    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel'):
            messages.warning(self.request, u"Редагування відмінено")
            return HttpResponseRedirect(reverse('groups'))
        else:
            return super(GroupUpdateView, self).post(request, *args, **kwargs)

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/groups_confirm_delete.html'
    def get_success_url(self):
        messages.warning(self.request, u"Групу %s видалено" %(self.object))
        return reverse('groups')
