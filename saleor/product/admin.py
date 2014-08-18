from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import (ProductImage, BagVariant, Bagx, ShirtVariant, Shirt,
                     Category, FixedProductDiscount, Color, BetSelection)
from .forms import ShirtAdminForm, ProductVariantInline, ImageInline


class ImageAdminInline(admin.StackedInline):
    model = ProductImage
    formset = ImageInline


class BagVariantInline(admin.StackedInline):
    model = BagVariant
    formset = ProductVariantInline


#class BagAdmin(admin.ModelAdmin):
#    inlines = [BagVariantInline, ImageAdminInline]


class ShirtVariantInline(admin.StackedInline):
    model = ShirtVariant
    formset = ProductVariantInline


class ShirtAdmin(admin.ModelAdmin):
    form = ShirtAdminForm
    list_display = ['name', 'collection', 'admin_get_price_min',
                    'admin_get_price_max']
    inlines = [ShirtVariantInline, ImageAdminInline]


class ProductCollectionAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Bagx)
admin.site.register(Shirt, ShirtAdmin)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(FixedProductDiscount)
admin.site.register(Color)

################# CJBET ####################
admin.site.register(BetSelection)