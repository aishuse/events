import stripe
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from customer.forms import EventForm
from customer.models import Event
from eventmanagement import settings
from .decorators import signin_required
from django.utils.decorators import method_decorator

stripe.api_key = settings.STRIPE_SECRET_KEY


@method_decorator(signin_required, name='dispatch')
class CustomerHome(TemplateView):
    template_name = 'customer/custhome.html'


@method_decorator(signin_required, name='dispatch')
class EventAdd(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'customer/add_event.html'
    success_url = '/customer/order/proceed'
    context_object_name = 'events'

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super(EventAdd, self).form_valid(form)


@method_decorator(signin_required, name='dispatch')
class GatewayView(TemplateView):
    template_name = "customer/stripe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # event = Event.objects.filter(host=self.request.user, id=kwargs['id'])
        context['amount'] = 1500 *100
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request, amount=None, *args, **kwargs):
    if request.method == "POST":
        # event = Event.objects.filter(host=request.user)

        payment_intent = stripe.PaymentIntent.create(

            amount=1500 *100,
            currency="INR",
            description="Publish Event",
            payment_method_types=["card"],
        )
        event = Event.objects.filter(status="NOT_PUBLISHED", host=request.user)

        for i in event:
            i.status = 'PUBLISHED'
            i.save()
        return render(request, 'customer/payment.html', payment_intent)
    return render(request, 'customer/payment.html')


@method_decorator(signin_required, name='dispatch')
class EventList(ListView):
    model = Event
    template_name = 'customer/eventlist.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(status='PUBLISHED')


@method_decorator(signin_required, name='dispatch')
class MyEventList(ListView):
    model = Event
    template_name = 'customer/my_events.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(status='PUBLISHED',host=self.request.user)


@method_decorator(signin_required, name='dispatch')
class UpdateEvent(UpdateView):
    model = Event
    template_name = 'customer/update_event.html'
    form_class = EventForm
    success_url = '/customer/myevent/list'


@method_decorator(signin_required, name='dispatch')
class DeleteEvent(DeleteView):
    model = Event
    template_name = 'customer/delete.html'
    success_url = '/customer/myevent/list'





