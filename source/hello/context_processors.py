from django.urls import translate_url
from django.conf import settings


def strip_language_code(request):
    language_base_link = request.path.split('/')[2:]
    return {'language_base_link': '/' + '/'.join(language_base_link)}
