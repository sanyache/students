#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.template.loader import render_to_string
from django.forms import ModelForm
from django.views import View
from django.views.generic import UpdateView, DeleteView, ListView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from ..models import Student, Group
from ..util import paginate, get_current_group
from django.utils.translation import ugettext as _
import json

def students_list(request):
    current_group = get_current_group(request)
    if current_group :
        students = Student.objects.filter(student_group=current_group)
    else:
     students = Student.objects.all()
    order_by = request.GET.get('order_by', '')
    if request.method == 'POST':
        search = request.POST.get('search_student')
        search_field = request.POST.get('search_field')
        if search_field == 'last_name':
            students = Student.objects.filter(last_name__iexact=search)
        if search_field == 'first_name':
            students = Student.objects.filter(first_name__iexact=search)
        if search_field == 'ticket':
            students = Student.objects.filter(ticket__exact=search)
        if search_field == 'student_group':
            students = Student.objects.filter(student_group__title__iexact=search)
        if students:
            return render(request, 'students/students_list.html',{'students': students})
        else:
            messages.info(request, _(u"Student not founded"))
            return HttpResponseRedirect(reverse('home'))


    if order_by in ('last_name', 'first_name','ticket'):
        students = students.order_by(order_by)
    elif order_by in ('student_group'):
        students = students.order_by('student_group__title')
    if request.GET.get('reverse','') == '1':
        students = students.reverse()
    context = paginate(students, 5, request, {}, var_name='students')
    return render(request, 'students/students_list.html', context)

def students_add(request):
    if request.method == "POST":
        if request.POST.get('add_button') is not None:
            errors = {}
            data={'middle_name': request.POST.get('middle_name'), 'notes': request.POST.get('notes')}


            first_name=request.POST.get('first_name','').strip()
            if not first_name:
                errors['first_name'] = _(u"First name is required")
            else:
                data['first_name'] = first_name
            last_name=request.POST.get('last_name','').strip()
            if not last_name:
                errors['last_name'] = _(u"Last name is required")
            else:
                data['last_name'] = last_name
            birthday=request.POST.get('birthday','').strip()
            if not birthday:
                errors['birthday'] = _(u"Birthday field is required")
            else:
                data['birthday'] = birthday
            ticket=request.POST.get('ticket','').strip()
            if not ticket:
                errors['ticket'] = _(u"Number of ticket is required")
            else:
                data['ticket'] = ticket
            student_group= request.POST.get('student_group','').strip()
            if not student_group:
                errors['student_group']= _(u"Select group")
            else:
                data['student_group']= Group.objects.get(pk=student_group)
            photo=request.FILES.get('photo')
            if photo:
                if photo.size > 2*1024*1024:
                    errors['photo'] = _(u"Size of photo should not exceed 2Мб")
                if photo.content_type not in ['image/jpeg','image/jpg','image/png']:
                    errors['photo'] = _(u"Only type file jpeg, jpg, png")
                data['photo'] = photo
            if not errors:
                student = Student(**data)
                student.save()
                messages.info(request,(_(u"Student {0} {1} added successfully").format(student.first_name,student.last_name)))
                return HttpResponseRedirect(reverse('home'))
            else:
                return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title'),'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            messages.info(request,(_(u"Student addition canceled")))
            return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title')})

class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = reverse('students_edit', kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-5'

        self.helper.layout[-1] = FormActions(
            Submit('add_button', _(u"Save "), css_class="btn btn-primary"),
            Submit('cancel_button', _(u"Cancel"), css_class="btn btn-link"),
        )

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm

    def get_success_url(self):
        messages.info(self.request, _(u"Student update successfully"))
        return reverse('home')
    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(request, _(u"Student update canceled"))
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'

    def get_success_url(self):
        messages.warning(self.request, _(u"Student %s  deleted") %(self.object))
        return reverse('home')

class Search(View):

    def get(self, request):
        q = request.GET.get('q', '')
        students = Student.objects.filter(last_name__icontains= q)
        name_list = []
        for student in students:
            new = {'q':student.last_name}
            if not new in name_list:
                name_list.append(new)
        return HttpResponse(json.dumps(name_list), content_type="application/json")

class StudentSearch(ListView):
    model = Student
    template_name = 'students/students_search.html'

    def post(self, request):
        search = request.POST.get('search_student')
        students = Student.objects.filter(last_name__iexact=search)
        context = {'students': students}
        return_str = render_to_string('students/part_views/part_search.html', context)
        return HttpResponse(json.dumps(return_str), content_type='application/json')