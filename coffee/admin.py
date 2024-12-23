from django.contrib import admin
from . models import Coffee, Category, Customer, Product,Order

# Register your models here.
class coffeeAdmin(admin.ModelAdmin):
    list_display=('name', 'price','quantity')
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Coffee, coffeeAdmin)