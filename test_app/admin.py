from django.contrib import admin

# Register your models here.
from test_app.models import Category, Product, Review

class ProductInLine(admin.StackedInline):
    model = Product
    fields = "title price".split()
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInLine]


class ProductAdmin(admin.ModelAdmin):
    List_display = 'id title description price products'.split()
    List_filter = 'price product'.split()
    List_editable = 'price'.split()


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)