from django.contrib import admin
from .models import *


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author')
    search_fields = ['title']


admin.site.register(Customer)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
