# from django.contrib import admin
# from .models import related models


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
from django.contrib import admin
from .models import CarMake, CarModel


# Inline class for CarModel so you can edit models inside CarMake admin
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # number of empty CarModel forms to display


# Admin class for CarModel (standalone)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'year', 'dealer_id', 'car_make')
    list_filter = ('type', 'year', 'car_make')
    search_fields = ('name',)


# Admin class for CarMake, with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    inlines = [CarModelInline]  # shows CarModels under CarMake


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
