from django.urls import path, include

urlpatterns = [
    path('v1/', include('cars.api.v1.urls'))
]
