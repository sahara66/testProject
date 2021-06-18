from django.contrib import admin
from test_app.models import Category, Product, Review
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)