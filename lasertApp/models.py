from __future__ import unicode_literals

import django
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
from django.utils.translation import ugettext_lazy as _

MANAGED = True


class Clients(models.Model):
    logo = models.ImageField(upload_to=settings.IMG_CLIENTS, verbose_name='Client Logo')
    url = models.URLField(verbose_name='Client website', null=True,blank=True)

    class Meta:
        managed = MANAGED
        db_table = 'clients'
        verbose_name_plural = 'Clients'


class SolutionCategory(models.Model):
    category_name_en = models.CharField(max_length=150, null=False)
    category_name_ar = models.CharField(max_length=150, null=False)

    def __unicode__(self):
        return self.category_name_en

    @property
    def getItemName(self):
        if django.utils.translation.get_language() == 'en':
            return self.category_name_en
        return self.category_name_ar

    class Meta:
        managed = MANAGED
        db_table = 'solution_category'
        verbose_name_plural = 'Solution category'


class Solutions(models.Model):
    name_en = models.CharField(max_length=150, null=False)
    name_ar = models.CharField(max_length=150, null=False)
    logo = models.ImageField(upload_to=settings.IMG_SERVICE)
    category = models.ForeignKey(SolutionCategory, related_name='solution_category', db_column='category_id')
    show_in_home_page = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name_en

    @property
    def getItemName(self):
        if django.utils.translation.get_language() == 'en':
            return self.name_en
        return self.name_ar

    class Meta:
        managed = MANAGED
        db_table = 'solutions'
        verbose_name_plural = 'Solutions'


class Serivces(models.Model):
    service_name_en = models.CharField(max_length=150, null=False)
    service_name_ar = models.CharField(max_length=150, null=False)
    icon = models.CharField(max_length=150,
                            help_text='Please user this website to grap your icon <a href="https://material.io/icons/" target="_blank">Icons</a>')
    description_en = models.TextField()
    description_ar = models.TextField()
    created_date = models.DateTimeField(default=django.utils.timezone.now)
    logo = models.ImageField(upload_to=settings.IMG_SERVICE)

    def __unicode__(self):
        return self.service_name_en

    @property
    def getItemName(self):
        print django.utils.translation.get_language()
        if django.utils.translation.get_language() == 'en':
            return self.service_name_en
        return self.service_name_ar

    @property
    def getItemDesc(self):
        if django.utils.translation.get_language() == 'en':
            return self.description_en
        return self.service_name_ar

    class Meta:
        managed = MANAGED
        ordering = ['-created_date']
        db_table = 'services'
        verbose_name_plural = 'Services'


class Partners(models.Model):
    logo = models.ImageField(upload_to=settings.IMG_PARTNERS, verbose_name='Partner Logo')
    url = models.URLField(verbose_name='partner website')

    class Meta:
        managed = MANAGED
        db_table = 'partners'
        verbose_name_plural = 'Partners'


class Recommends(models.Model):
    name = models.CharField(max_length=150, null=False)
    company = models.CharField(max_length=150, null=False)
    comment = models.TextField()
    logo = models.ImageField(upload_to=settings.IMG_RECOMMEND, verbose_name='Partner Logo')

    def __unicode__(self):
        return self.name

    class Meta:
        managed = MANAGED
        db_table = 'recommendations'
        verbose_name_plural = 'Recommendations'


class Mailer(models.Model):
    email = models.EmailField(max_length=150)
    group = models.CharField(max_length=150, choices=[('1', _("New Customer")), ('2', _("Sales Service"))])

    def __unicode__(self):
        return self.email

    class Meta:
        managed = MANAGED
        db_table = 'mailers'
        verbose_name_plural = 'mailers'


class Careers(models.Model):
    job_title = models.CharField(max_length=150, null=False, unique=True)
    job_sector = models.CharField(max_length=150, null=False)
    years_of_experience = models.CharField(max_length=150, null=False)
    location = models.CharField(max_length=150, null=False)
    job_description = models.TextField()
    job_skills = models.TextField()
    is_active = models.BooleanField(default=True)
    job_mail = models.EmailField(null=False)
    create_date = models.DateTimeField(default=django.utils.timezone.now)

    def __unicode__(self):
        return self.job_title

    class Meta:
        managed = MANAGED
        db_table = 'careers'
        verbose_name_plural = 'Careers'
        ordering = ['-create_date']


class Subscribers(models.Model):
    mail = models.EmailField(null=False, unique=True)

    def __unicode__(self):
        return self.mail

    class Meta:
        managed = MANAGED
        db_table = 'subscribers'
        verbose_name_plural = 'Subscribers'


class Slider(models.Model):
    img = models.ImageField(upload_to=settings.IMG_SLIDER)
    title_ar = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)
    description_ar = models.CharField(max_length=150)
    description_en = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title_ar

    @property
    def getItemName(self):
        print django.utils.translation.get_language()
        if django.utils.translation.get_language() == 'en':
            return self.title_en
        return self.title_ar

    @property
    def getItemDesc(self):
        print django.utils.translation.get_language()
        if django.utils.translation.get_language() == 'en':
            return self.description_en
        return self.description_ar

    class Meta:
        managed = MANAGED
        db_table = 'sliders'
        verbose_name_plural = 'Home sliders'


class About(models.Model):
    section_one_title  = models.CharField(max_length=150)
    section_one_description = models.TextField()
    section_one_first_image = models.ImageField(upload_to=settings.IMG_ABOUT)
    section_one_second_image = models.ImageField(upload_to=settings.IMG_ABOUT)

    section_two_title  = models.CharField(max_length=150)
    section_two_description_html = models.TextField()
    section_two_first_image = models.ImageField(upload_to=settings.IMG_ABOUT)
    section_two_second_image = models.ImageField(upload_to=settings.IMG_ABOUT)

    section_three_description_html = models.TextField()
    section_three_second_image = models.ImageField(upload_to=settings.IMG_ABOUT)

    section_one_title_arabic = models.CharField(max_length=150)
    section_one_description = models.TextField()
    section_one_first_image = models.ImageField(upload_to=settings.IMG_ABOUT)
    section_one_second_image = models.ImageField(upload_to=settings.IMG_ABOUT)

    section_two_title = models.CharField(max_length=150)
    section_two_description_html = models.TextField()
    section_two_first_image = models.ImageField(upload_to=settings.IMG_ABOUT)
    section_two_second_image = models.ImageField(upload_to=settings.IMG_ABOUT)

    section_three_description_html = models.TextField()
    section_three_second_image = models.ImageField(upload_to=settings.IMG_ABOUT)

    def __unicode__(self):
        return str(self.pk)+'- Click to edit'

    class Meta:
        managed = MANAGED
        db_table = 'about'
        verbose_name_plural = 'About us page'

