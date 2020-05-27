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

@register.simple_tag
def categorias_div():
    """
    section banner
    :return:
    """
    items = Categoria.objects.filter(is_active=True).order_by('Nombre')
    items_div = ""
    item_div_list = ""
    for i, j in enumerate(items):
        if not i % 2:
            items_div += """<div class="block1 hov-img-zoom pos-relative m-b-30"><img src="/media/{}" alt="IMG-BENNER"><div class="block1-wrapbtn w-size2"><a href="/{}" class="flex-c-m size2 m-text2 bg3 hov1 trans-0-4">{}</a></div></div>""".format(
                j.Img_categoria, j.Slug, j.Nombre)
        else:
            items_div_ = """<div class="block1 hov-img-zoom pos-relative m-b-30"><img src="/media/{}" alt="IMG-BENNER"><div class="block1-wrapbtn w-size2"><a href="/{}" class="flex-c-m size2 m-text2 bg3 hov1 trans-0-4">{}</a></div></div>""".format(
                j.Img_categoria, j.Slug, j.Nombre)
            item_div_list += """<div class="col-sm-10 col-md-8 col-lg-4 d-inline-block">""" + items_div + items_div_ + """</div>"""
            items_div = ""

    return mark_safe(item_div_list)
