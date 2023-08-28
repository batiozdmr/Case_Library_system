from django.utils.translation import get_language

from apps.main.parameter.models import Menu, SiteSettings


def site(request):
    site_settings = SiteSettings.objects.last()
    urlObject = request.get_host()
    url = request.build_absolute_uri()
    return {'site_settings': site_settings, 'showURL': urlObject, 'URL': url, }


def menu(request):
    menu = Menu.objects.filter().order_by('alignment')
    lang = get_language()
    return {'menu': menu, 'lang': lang}
