from django.contrib import admin

from samples.models import Product, TestType, TestingParameter

class TestParaInline(admin.StackedInline):

    model=TestingParameter
    extra=0


class ProductAdmin(admin.ModelAdmin):
    search_fields = ("product_name",)
    inlines= (TestParaInline,)

class TestParaAdmin(admin.ModelAdmin):
    search_fields = ("product_name",)
    list_display=('testing_parameters', 'product')

admin.site.register(Product, ProductAdmin)
admin.site.register(TestType)
admin.site.register(TestingParameter, TestParaAdmin)