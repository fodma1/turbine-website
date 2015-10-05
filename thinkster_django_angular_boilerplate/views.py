import requests
import json

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator


def contact_us(request):
    data = json.loads(request.body)
    name = data['name']
    email = data['email']
    message = data['message']

    compiled_message = 'Name: {name}\nEmail: {email}\n\nMessage:{message}'.format(name=name, email=email, message=message)

    response = requests.post(
        settings.MAILGUN_API_URL + '/messages',
        data={'from': 'Mailgun Sandbox <{sender}>'.format(sender=settings.MAILGUN_SMTP_LOGIN),
              'to': settings.EMAIL_RECIPIENTS,
              'subject': 'New contact message',
              'text': compiled_message})

    response.raise_for_status()

    return HttpResponse()


class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)
