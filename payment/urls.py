from django.urls import path
from . import views
from . import webhooks
from django.utils.translation import gettext_lazy as _


app_name = 'payment'

urlpatterns = [
    path(_('process/'), views.PaymentProcessView.as_view(), name='process'),
    path(_('completed/'), views.payment_completed, name='completed'),
    path(_('canceled/'), views.payment_canceled, name='canceled'),
]