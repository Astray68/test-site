from .models import MenuItem


def menu_items(request):
    navbar_items = MenuItem.objects.all().order_by('order')
    footer_items = navbar_items.filter(show_in_footer=True)
    return {'navbar_items': navbar_items, 'footer_items': footer_items}