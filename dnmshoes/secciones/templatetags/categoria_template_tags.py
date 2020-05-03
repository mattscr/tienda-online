from django import template
from secciones.models import Categoria
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def categoria():
    items = Categoria.objects.all()
    items_li = ""
    for i in items:
        items_li += """<li class="nav-item"><a class="nav-link" href="/{}/">{}</a></li>""".format(
            i.Slug, i.Nombre)
    return mark_safe(items_li)
