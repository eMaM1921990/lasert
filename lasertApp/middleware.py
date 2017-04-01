from datetime import timedelta

from django.core.cache import cache
from django.utils import timezone

class OnlineNowMiddleware(object):

    def process_request(self, request):
        # current date
        print '---------'
        print timezone.datetime.today().date()
        current_date = timezone.datetime.today().date()
        print '---------'
        # Check the IP address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            user_ip = x_forwarded_for.split(',')[0]
        else:
            user_ip = request.META.get('REMOTE_ADDR')
        # Get the list of the latest online users
        online = cache.get('online_now')
        visitors = cache.get('visitors')
        today_visit = cache.get(current_date)
        # Check the active IP addresses
        if online:
            online = [ip for ip in online if cache.get(ip)]
        else:
            online = []

        if not visitors:
            visitors=[]

        if not today_visit:
            today_visit = []

        # Add the new IP to cache
        cache.set(user_ip, user_ip, 600)
        # Add the new IP to list if doesn't exist
        if user_ip not in online:
            online.append(user_ip)

        visitors.append(user_ip)
        today_visit.append(user_ip)

        # Set the new online list
        cache.set('online_now', online)
        cache.set('visitor', visitors)
        cache.set(current_date, today_visit)
        # Add the number of online users to request
        request.__class__.online_now = len(online)
        request.__class__.visitor = len(visitors)
        request.__class__.today_visit = len(today_visit)
