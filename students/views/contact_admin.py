# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from  django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from studentsdb.settings import ADMIN_EMAIL
from ..forms import ContactForm

def contact_admin(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])
            except Exception:
                messages.warning(request,u"Під час відправки виникла помилка. Спробуйте ще раз")
            else:
                messages.info(request,u"Повідомлення успішно надіслане")
            return HttpResponseRedirect(reverse('contact_admin'))
    else:
        form = ContactForm()
    return render(request, 'contact_admin/form.html', {'form': form})