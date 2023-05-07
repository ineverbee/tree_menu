from django import template
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from ..models import Menu


register = template.Library()


# Тег извлекает значения из базы
@register.simple_tag()
def draw_menu(uri):
    dirs = uri.split('-')

    # Регулярное выражение для извлечения всех записей в базе с подходящим parent_uri
    # ^(?:some_menu)(?:-some_dir1)?(?:-some_dir2)? ... (?:-leaf)?$
    # Примеры подходящих parent_uri: some_menu, some_menu-some_dir1, some_menu-some_dir1-some_dir2
    regexp = r'^(?:'+dirs[0]+')'
    regexp += ''.join([f'(?:-{s})?' for s in dirs[1:]])+'$'

    menu = Menu.objects.filter(
        parent_uri__regex=regexp,
    ).order_by('uri')

    if menu:
        # Добавляет уровень вложенности для отрисовки отступа
        for item in menu:
            item.level = item.uri.count('-')
        return menu
    else:
        raise Http404