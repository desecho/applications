# -*- coding: utf8 -*-
from django.shortcuts import render_to_response, redirect
from applications.models import Record, Department, SubscriberStatus, Type, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django-annoying import render_to


def logout_view(request):
    logout(request)
    return redirect('/login/')


@render_to('index.html')
@login_required
def index(request):
    message = ''
    if request.method == 'POST':
        types = request.POST.getlist('types')
        if not request.POST['appartment']:
            appartment = None
        else:
            appartment = request.POST['appartment']
        house = request.POST['house']
        if request.POST['building']:
            house += '/' + request.POST['building']
        for type in types:
            r = Record(user_id=request.user.id,
                       street=request.POST['street'],
                       house=house,
                       phone=request.POST['phone'],
                       contact=request.POST['contact'],
                       type=Type.objects.get(pk=type),
                       subscriber_status=SubscriberStatus.objects.get(pk=request.POST['subscriber_status']),
                       comment=request.POST['comment'],
                       name=request.POST['name'],
                       appartment=appartment)
            r.save()
        message = 'Заявка добавлена.'
    departments = Department.objects.all()
    types = Type.objects.all()
    subscriber_statuses = SubscriberStatus.objects.all()
    return {'departments': departments,
            'types': types,
            'subscriber_statuses': subscriber_statuses,
            'message': message}