# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import Exam
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView

def exams_list(request):
    exams = Exam.objects.all()
    return render(request, 'students/exams_list.html', {'exams': exams})

class ExamCreateView(CreateView):
    model = Exam
    template_name = 'students/exams_add.html'
    fields = '__all__'
    def get_success_url(self):
        messages.info(self.request, u"Екзамен успішно добавлений")
        return reverse('exams')
    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel'):
            messages.warning(self.request, u"Створення екзамену відмінено")
            return HttpResponseRedirect(reverse('exams'))
        else:
            return super(ExamCreateView,self).post(request, *args, **kwargs)

class ExamUpdateView(UpdateView):
    model = Exam
    template_name = 'students/exams_edit.html'
    fields = '__all__'
    def get_success_url(self):
        messages.info(self.request, u"Екзамен успішно збережений")
        return reverse('exams')
    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel'):
            messages.warning(self.request, u"Редагування відмінено")
            return HttpResponseRedirect(reverse('exams'))
        else:
            return super(ExamUpdateView, self).post(request, *args, **kwargs)

class ExamDeleteView(DeleteView):
    model = Exam
    template_name = 'students/exams_confirm_delete.html'
    def get_success_url(self):
        messages.warning(self.request, u"Екзамен %s видалено" %(self.object))
        return reverse('exams')
