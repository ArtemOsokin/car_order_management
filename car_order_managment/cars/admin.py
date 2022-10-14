from cars.models import Color, CarBrand, CarModel, Order
from django.contrib import admin


class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 0


class OrderInline(admin.TabularInline):
    model = Order
    extra = 0


# Create your tests here.
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    # отображение полей в списке
    list_display = ('name', 'id',)

    # фильтрация в списке
    list_filter = ('name',)

    # поиск по полям
    search_fields = ('name', 'id',)

    # порядок следования полей в форме создания/редактирования
    fields = (
        'name',
    )
    inlines = [
        OrderInline
    ]


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    # отображение полей в списке
    list_display = ('name', 'id',)

    # фильтрация в списке
    list_filter = ('name',)

    # поиск по полям
    search_fields = ('name', 'id',)

    # порядок следования полей в форме создания/редактирования
    fields = (
        'name',
    )
    inlines = [
        CarModelInline,
    ]


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    # отображение полей в списке
    list_display = ('name', 'id',)

    # фильтрация в списке
    list_filter = ('name',)

    # поиск по полям
    search_fields = ('name', 'id',)

    # порядок следования полей в форме создания/редактирования
    fields = (
        'name', 'car_brand'
    )
    inlines = [
        OrderInline
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # отображение полей в списке
    list_display = ('id', 'car_model', 'color', 'amount', 'data_order')

    # фильтрация в списке
    list_filter = ('amount', 'data_order')

    # поиск по полям
    search_fields = ('amount', 'data_order')

    # порядок следования полей в форме создания/редактирования
    fields = (
        'amount', 'data_order', 'color', 'car_model'
    )
