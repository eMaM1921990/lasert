from django.contrib.sessions.models import Session
from django.utils import timezone


def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now()).count()
    return active_sessions


def get_today_users():
    today_sessions = Session.objects.filter(expire_date__gte=timezone.datetime.today().date()).count()
    return today_sessions

def get_all_users():
    return Session.objects.count()


