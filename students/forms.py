# -*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(label=u'Ваша емейл адреса')
    subject = forms.CharField(label=u'Заголовок листа', max_length=128)
    message = forms.CharField(label=u"Текст повідомлення", widget=forms.Textarea)