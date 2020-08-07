from django import template
# В template.Library зарегистрированы все теги и фильтры шаблонов
# добавляем к ним и наш фильтр
register = template.Library()


@register.filter 
def addclass(field, css,placeholder):

    return field.as_widget(attrs={"class": css,'placeholder':placeholder})


