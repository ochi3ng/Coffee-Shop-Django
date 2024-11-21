from django.contrib import admin
from . models import Coffee, category, Customer, Product,Order

# Register your models here.
class coffeeAdmin(admin.ModelAdmin):
    list_display=('name', 'price','quantity')
admin.site.register(category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Coffee, coffeeAdmin)