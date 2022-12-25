import itertools

from django import template

register = template.Library()


@register.filter
def parts(value, part_length):
    """
    Breaks a list up into a list of lists of size <chunk_length>
    """
    clean = int(part_length)
    i = iter(value)
    while True:
        part = list(itertools.islice(i, clean))
        if part:
            yield part
        else:
            break