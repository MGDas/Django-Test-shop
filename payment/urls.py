from django.urls import path
from .views import PaymentProcess, PaymentDone, PaymentCanceled


urlpatterns = [
    path('process/', PaymentProcess, name='process_url'),
    path('done/', PaymentDone, name='done_url'),
    path('canceled/', PaymentCanceled, name='canceled_url'),
]
