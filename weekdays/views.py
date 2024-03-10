from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _


def weekdays_all(request):
    weekdays = [_('Monday'), _('Tuesday'), _('Wednesday'), _('Thursday'), _('Friday'), _('Saturday'), _('Sunday')]
    return render(request, 'weekdays/weekdays.html', {'weekdays': weekdays})


def weekdays_lang(request, lang=None):
    if lang == 'uz':
        days = [_('Dushanba'), _('Seshanba'), _('Chorshanba'), _('Payshanba'), _('Juma'), _('Shanba'), _('Yakshanba')]
    elif lang == 'en':
        days = [_('Monday'), _('Tuesday'), _('Wednesday'), _('Thursday'), _('Friday'), _('Saturday'), _('Sunday')]
    elif lang == 'ru':
        days = [_('Понедельник'), _('Вторник'), _('Среда'), _('Четверг'), _('Пятница'), _('Суббота'), _('Воскресенье')]
    elif lang is None:
        days = [_('Monday'), _('Tuesday'), _('Wednesday'), _('Thursday'), _('Friday'), _('Saturday'), _('Sunday')]
    else:
        return HttpResponse("Invalid language code")
    return render(request, 'weekdays/weekdays.html', {'weekdays': days})
