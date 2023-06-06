from django import template
from toko.models import OrderProdukItem, Order

register = template.Library()

@register.filter
def total_produk_dikeranjang(user):
    if user.is_authenticated:
        query = Order.objects.filter(user=user, ordered=False)
        item = OrderProdukItem.objects.filter(user=user, ordered=False)
        if query.exists():
            order = query[0]
            total_quantity = 0
            for item in order.produk_items.all():
                total_quantity += item.quantity
            return total_quantity
    return 0
