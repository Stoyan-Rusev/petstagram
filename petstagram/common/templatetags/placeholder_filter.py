from django import template

register = template.Library()


@register.filter
def add_placeholder(form_field, value):
    return form_field.as_widget(attrs={'placeholder': value})
