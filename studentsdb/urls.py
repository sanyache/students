"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from students.views import students,groups,exams, contact_admin
from students.views.students import StudentUpdateView,StudentDeleteView,Search,StudentSearch
from students.views.groups import GroupCreateView, GroupUpdateView,GroupDeleteView
from students.views.exams import ExamCreateView, ExamUpdateView, ExamDeleteView
from students.views.journal import JournalView
from students.views.rest import StudentListAPI, StudentDetailAPI
from accounts import views as accounts_views
from settings import MEDIA_ROOT, DEBUG
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    url(r'^$', students.students_list, name='home'),
    url(r'^students/add/$', students.students_add, name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),

    url(r'^students/api/$', StudentListAPI.as_view()),
    url(r'^students/api/(?P<pk>[0-9]+)/$', StudentDetailAPI.as_view()),
    url(r'^students/search/$', Search.as_view(), name='search'),
    url(r'^students/student_search/$', StudentSearch.as_view(), name='student_search'),

    url(r'^groups/$', groups.groups_list, name='groups'),
    url(r'^groups/add/$', GroupCreateView.as_view(), name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$', GroupUpdateView.as_view(), name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$',GroupDeleteView.as_view(), name='groups_delete'),     

    url(r'^exams/$', exams.exams_list, name='exams'),
    url(r'^exams/add/$', ExamCreateView.as_view(), name='exams_add'),
    url(r'^exams/(?P<pk>\d+)/edit/$', ExamUpdateView.as_view(), name='exams_edit'),
    url(r'^exams/(?P<pk>\d+)/delete/$', ExamDeleteView.as_view(), name='exams_delete'),
    
    url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),

    url(r'^contact_admin/$', contact_admin.contact_admin, name='contact_admin'),

    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='students/login.html'), name='login'),
    url(r'^settings/account/$', accounts_views.update_profile, name='my_account'),
    
    url(r'^reset/$', auth_views.PasswordResetView.as_view(template_name='students/password_reset.html',	email_template_name='students/password_reset_email.html', subject_template_name='students/password_reset_subject.txt'), name='password_reset'),
    url(r'^reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='students/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',	auth_views.PasswordResetConfirmView.as_view(template_name='students/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset/complete/$', auth_views.PasswordResetCompleteView.as_view(template_name='students/password_reset_complete.html'),name='password_reset_complete'),
    
    url(r'^oauth/', include('social_django.urls', namespace='social')),    

    url(r'^admin/', admin.site.urls),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)