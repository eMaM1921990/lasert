import django
from django.template.defaultfilters import stringfilter
from django import template

register = template.Library()


@register.filter
@stringfilter
def serviceDescLocalize(service):
    currentLang = django.utils.translation.get_language()
    if currentLang == 'en-us':
        return service.description_en
    else:
        return service.description_ar


@register.filter
@stringfilter
def categoryLocalize(service):
    currentLang = django.utils.translation.get_language()
    if currentLang == 'en-us':
        return service.category_name_en
    else:
        return service.category_name_ar


@register.filter
@stringfilter
def solutionLocalize(solution):
    currentLang = django.utils.translation.get_language()
    if currentLang == 'en-us':
        return solution.name_en
    else:
        return solution.name_ar
