import requests
import json
import settings

from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator


def contact_us(request):
    data = json.loads(request.body)
    name = data['name']
    email = data['email']
    message = data['message']
    
    response = requests.post(
        'https://api.mailgun.net/v3/sandboxdbf93f180e6e40ffbb8eafbc80fbc2d3.mailgun.org/messages',
        auth=('api', settings.MAILGUN_API_KEY),
        data={'from': 'Mailgun Sandbox <postmaster@sandboxdbf93f180e6e40ffbb8eafbc80fbc2d3.mailgun.org>',
              'to': 'Matyas <matyas.fodor@gmail.com>, Turbine <turbines@googlegroups.com>',
              'subject': 'Contact form',
              'text': 'Name: {name}\nEmail: {email}\n\nMessage:{message}'.format(name=name, email=email, message=message)})

    response.raise_for_status()

    return HttpResponse


def send_simple_message(request):
    return requests.post(
        'https://api.mailgun.net/v3/sandboxdbf93f180e6e40ffbb8eafbc80fbc2d3.mailgun.org/messages',
        auth=('api', 'key-385acf1d49046d4fee3665e639f1b6fb'),
        data={'from': 'Mailgun Sandbox <postmaster@sandboxdbf93f180e6e40ffbb8eafbc80fbc2d3.mailgun.org>',
              'to': 'Matyas <matyas.fodor@gmail.com>',
              'subject': 'Hello Matyas',
              'text': 'Congratulations Matyas, you just sent an email with Mailgun!  You are truly awesome!  You can see a record of this email in your logs: https://mailgun.com/cp/log .  You can send up to 300 emails/day from this sandbox server.  Next, you should add your own domain so you can send 10,000 emails/month for free.'})


class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)
