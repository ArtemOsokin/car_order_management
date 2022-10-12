from django.urls import path, include

urlpatterns = [
    path('colors/', include('cars.api.v1.colors.urls')),
    path('models/', include('cars.api.v1.models.urls')),
    path('brands/', include('cars.api.v1.brands.urls')),
    path('orders/', include('cars.api.v1.orders.urls'))
]
