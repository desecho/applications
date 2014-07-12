# -*- coding: utf8 -*-

from django.db import models
from django.contrib.auth.models import User


class Type(models.Model):
    name = models.CharField('название', max_length=255)

    class Meta:
        verbose_name = 'тип заявки'
        verbose_name_plural = 'типы заявок'

    def __unicode__(self):
        return self.name


class SubscriberStatus(models.Model):
    name = models.CharField('название', max_length=2)

    class Meta:
        verbose_name = 'тип абонента'
        verbose_name_plural = 'типы абонентов'

    def __unicode__(self):
        return self.name


class Department(models.Model):
    name = models.CharField('название', max_length=255)

    class Meta:
        verbose_name = 'отдел'
        verbose_name_plural = 'отделы'

    def __unicode__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField('название', max_length=255)

    class Meta:
        verbose_name = 'приоритет'
        verbose_name_plural = 'приоритеты'

    def __unicode__(self):
        return self.name


class Record(models.Model):
    user = models.ForeignKey(User, verbose_name='пользователь')
    name = models.CharField('название', max_length=255, blank=True)
    street = models.CharField('улица', max_length=255)
    house = models.CharField('дом', max_length=255)
    appartment = models.IntegerField('квартира', null=True, blank=True)
    phone = models.BigIntegerField('телефон', max_length=11)
    contact = models.CharField('имя контакта', null=True, blank=True,
                               max_length=255)
    request_date = models.DateField('дата заявки', auto_now_add=True)
    type = models.ForeignKey(Type, verbose_name='тип заявки')
    subscriber_status = models.ForeignKey(SubscriberStatus,
                                          verbose_name='тип абонента')
    department = models.ForeignKey(Department, null=True, blank=True,
                                   verbose_name='отдел')
    priority = models.ForeignKey(Priority, default=2, verbose_name='приоритет')
    monthly_payment = models.CharField('абон. плата', max_length=255, null=True,
                                       blank=True)
    speed = models.CharField('скорость', max_length=255, null=True, blank=True)
    initial_payment = models.CharField('стоимость подключения', max_length=255,
                                       null=True, blank=True)
    connection_date = models.DateField('дата подключения', null=True,
                                       blank=True)
    comment = models.CharField('комментарий', max_length=255, blank=True)
    status = models.BooleanField('закрыта', default=False)

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'

    def __unicode__(self):
        return self.street + ' ' + self.house
