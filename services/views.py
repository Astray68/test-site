from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from .models import Category, Promotion, Product


class ServicesView(View):
    def get(self, request):
        promotion_list = Promotion.objects.filter(is_deleted=False)
        category_list = Category.objects.filter(is_deleted=False, parent=None)
        return render(request, 'services/services.html', {'category_list': category_list,
                                                          'promotion_list': promotion_list})


def category_view(request, slug):
    promotion_list = Promotion.objects.filter(is_deleted=False)
    category = get_object_or_404(Category, slug=slug, is_deleted=False)
    category_id = category.id
    category_list = Category.objects.filter(is_deleted=False, parent_id=category_id)
    product_list = Product.objects.filter(is_deleted=False, category_id=category_id)
    breadcrumbs = []
    _category = Category.objects.get(slug=slug)
    breadcrumbs.append(_category)
    while _category.parent_id:
        _category = Category.objects.get(is_deleted=False, id=_category.parent_id)
        breadcrumbs.append(_category)
    breadcrumbs.reverse()
    return render(request, 'services/category.html', {'category_list': category_list, 'product_list': product_list,
                                                      'promotion_list': promotion_list, 'breadcrumbs': breadcrumbs})
