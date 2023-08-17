from decimal import Decimal
import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse,\
                             get_object_or_404
from django.views import View

from orders.models import Order


# create the Stripe instance
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def payment_process(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        success_url = request.build_absolute_uri(
                        reverse('payment:completed'))
        cancel_url = request.build_absolute_uri(
                        reverse('payment:canceled'))
        # Stripe checkout session data
        session_data = {
            'mode': 'payment',
            'client_reference_id': order.id,
            'success_url': success_url,
            'cancel_url': cancel_url,
            'line_items': []
        }
        # create Stripe checkout session
        session = stripe.checkout.Session.create(**session_data)
        # redirect to Stripe payment form
        return redirect(session.url, code=303)
    else:
        return render(request, 'payment/process.html', locals())


class PaymentProcessView(View):

    @staticmethod
    def get_order_from_session(request):
        order_id = request.session.get('order_id', None)
        order = get_object_or_404(Order, id=order_id)
        return order_id

    def get(self, request, *args, **kwargs):
        order_id, order = self.get_order_from_session(request)
        return render(request, 'payment/process.html', locals())

    def post(self, request):
        order_id, order = self.get_order_from_session(request)
        success_url = request.build_absolute_uri(
            reverse('payment:completed')
        )
        cancel_url = request.build_absolute_uri(
            reverse('payment:canceled')
        )

        # Stripe checkout session data
        session_data = {
            'mode': 'payment',
            'client_reference_id': order_id,
            'success_url': success_url,
            'cancel_url': cancel_url,
            'line_items': []
        }

        # create Stripe checkout session
        session = stripe.checkout.Session.create(**session_data)

        # redirect to Stripe payment form
        return redirect(session.url, code=303)
