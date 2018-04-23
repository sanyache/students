# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _

class ContactForm(forms.Form):
    from_email = forms.EmailField(label=_(u'Your email address'))
    subject = forms.CharField(label=_(u'Head'), max_length=128)
    message = forms.CharField(label=_(u"Text area"), widget=forms.Textarea)