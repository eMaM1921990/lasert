from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
from lasertApp.forms import ContactUsForm
from lasertApp.models import Partners, Recommends, Clients, Solutions, Serivces, SolutionCategory, Careers, Subscribers, \
    Slider, About, ContactUs
from lasertApp.sessionManager import get_current_users, get_today_users, get_all_users
from django.utils.translation import ugettext_lazy as _


def index(request):
    template = 'index.html'
    context = {}
    context['partners'] = Partners.objects.all()[:15]
    context['services'] = Serivces.objects.all()[:4]
    context['recommends'] = Recommends.objects.all()[:4]
    context['solutions'] = Solutions.objects.filter(show_in_home_page=True)[:6]
    # context['online'] = get_current_users()
    # context['today'] = get_today_users()
    # context['all'] = get_all_users()
    context['sliders'] = Slider.objects.all()
    return render(request, template,context=context)


def contact_us(request):
    template = 'contact.html'
    context = {}
    if request.POST:
        form = ContactUsForm(request.POST)
        print 'pos'
        if form.is_valid():
            form.send_email()
            form = ContactUsForm
            messages.success(request, _('Thanks for your connect '))

    else:
        form = ContactUsForm
    context['form'] = form
    context['data'] = ContactUs.objects.all()[:1]
    return render(request, template, context=context)


def partner(request):
    template = 'partner.html'
    context = {}
    context['partners'] = Partners.objects.all()
    context['online'] = get_current_users()
    context['today'] = get_today_users()
    context['all'] = get_all_users()
    return render(request, template,context=context)


def clients(request):
    template = 'client.html'
    context = {}
    context['clients'] = Clients.objects.all()
    return render(request, template,context)


def solution(request):
    template = 'solutions.html'
    context = {}
    context['services'] = Serivces.objects.all()[:4]
    context['solutions'] = Solutions.objects.select_related().all()
    context['categories'] = SolutionCategory.objects.all()
    return render(request, template, context)


def careers(request):
    template = 'career.html'
    context = {}
    context['jobs'] = Careers.objects.filter(is_active=True)
    return render(request, template, context)


def about(request):
    template = 'about.html'
    context ={
        'about':About.objects.first()
    }
    return render(request, template,context)


def addToSubscriber(request):
    print 'Subscripe'
    if request.POST:
        try:
            Subscribers(mail=request.POST['email']).save()
        except Exception as e:
            print e
    return HttpResponse('OK')