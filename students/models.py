# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Student(models.Model):
    class Meta(object):
        ordering=['last_name']
        verbose_name = _(u"Student")
        verbose_name_plural = _(u'Students')
    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name = _(u"First name")
    )
    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name = _(u"Last name")
    )
    middle_name = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name=_(u"Middle name")
    )
    birthday = models.DateField(
        blank=False,
        null=True,
        verbose_name= _(u"Birthday")

    )
    photo = models.ImageField(
        blank=True,
        null=True,
        verbose_name= _(u"Photo")
    )
    ticket = models.CharField(
        max_length=30,
        blank=False,
        verbose_name= _(u"Ticket")
    )
    student_group = models.ForeignKey('Group',
        verbose_name= _(u"Group"),
        blank= False,
        null= True,
        on_delete= models.PROTECT
    )
    notes = models.TextField(
        blank=True,
        verbose_name= _(u"Notes")
    )

    def __unicode__(self):
        return u"%s%s"%(self.first_name, self.last_name)

class Group(models.Model):
    class Meta(object):
        verbose_name = _(u"Group")
        verbose_name_plural = _(u"Groups")
    title = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=_(u"Group name")
    )
    leader = models.OneToOneField('Student',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_(u"Leader"))
    def __unicode__(self):
        if self.leader:
            return u"%s(%s%s)"%(self.title, self.leader.first_name, self.leader.last_name)
        else:
            return u"%s"%(self.title)

class Exam(models.Model):
    class Meta(object):
        verbose_name = _(u"Exam")
        verbose_name_plural = _(u"Exams")

    date_exam = models.DateTimeField(
        blank= True,
        null= True,
        verbose_name= _(u"exam time")
    )
    teacher = models.CharField(
        max_length= 256,
        blank= True,
        verbose_name= _(u"Teacher")
    )
    group_exam= models.ForeignKey('Group',
        verbose_name= _(u"Group"),
        blank= True,
        null= True,
        on_delete= models.PROTECT
    )
    subject = models.CharField(
        blank= True,
        max_length= 256,
        verbose_name= _(u"Subject")
    )
    def __unicode__(self):
        return u"%s%s"%(self.subject, self.group_exam)
# Create your models here.

class MonthJournal(models.Model):
    class Meta:
        verbose_name = _(u'Month journal')
        verbose_name_plural = _(u'Month journals')

    student = models.ForeignKey('Student',
                                    verbose_name = _(u'Student'),
                                    blank = False,
                                    unique_for_month ='date')
    date = models.DateField(
            verbose_name = _(u'Date'),
            blank = False)
    present_day1 = models.BooleanField(default=False)
    present_day2 = models.BooleanField(default=False)
    present_day3 = models.BooleanField(default=False)
    present_day4 = models.BooleanField(default=False)
    present_day5 = models.BooleanField(default=False)
    present_day6 = models.BooleanField(default=False)
    present_day7 = models.BooleanField(default=False)
    present_day8 = models.BooleanField(default=False)
    present_day9 = models.BooleanField(default=False)
    present_day10 = models.BooleanField(default=False)
    present_day11 = models.BooleanField(default=False)
    present_day12 = models.BooleanField(default=False)
    present_day13 = models.BooleanField(default=False)
    present_day14 = models.BooleanField(default=False)
    present_day15 = models.BooleanField(default=False)
    present_day16 = models.BooleanField(default=False)
    present_day17 = models.BooleanField(default=False)
    present_day18 = models.BooleanField(default=False)
    present_day19 = models.BooleanField(default=False)
    present_day20 = models.BooleanField(default=False)
    present_day21 = models.BooleanField(default=False)
    present_day22 = models.BooleanField(default=False)
    present_day23 = models.BooleanField(default=False)
    present_day24 = models.BooleanField(default=False)
    present_day25 = models.BooleanField(default=False)
    present_day26 = models.BooleanField(default=False)
    present_day27 = models.BooleanField(default=False)
    present_day28 = models.BooleanField(default=False)
    present_day29 = models.BooleanField(default=False)
    present_day30 = models.BooleanField(default=False)
    present_day31 = models.BooleanField(default=False)

    def __unicode__(self):
         return u'%s: %d, %d' % (self.student.last_name, self.date.month, self.date.year)
