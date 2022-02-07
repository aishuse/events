from django.db.models import Count
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, TemplateView

from authapp.admin import UserCreationForm
from authapp.models import MyUser


class Home(TemplateView):
    template_name = 'authapp/home.html'


class AddCustomer(CreateView):
    model = MyUser
    form_class = UserCreationForm
    template_name = 'authapp/custsignup.html'
    success_url = '/accounts/login/'

    def form_valid(self, form):
        form.instance.role = 'CUSTOMER'
        return super(AddCustomer, self).form_valid(form)


class ListCutomers(ListView):
    model = MyUser
    template_name = 'authapp/customers.html'
    context_object_name = 'customers'

    def get_context_data(self, *args, **kwargs):
        user_posts = MyUser.objects.annotate(total_posts=Count('event'))
        context = super(ListCutomers, self).get_context_data(*args, **kwargs)
        context['user_posts'] = user_posts
        return context


def loghome(request):
    if request.user.is_authenticated:
        if request.user.role == 'CUSTOMER':

            return redirect('eventlist')
        else:
            return redirect('home')
    return render(request, 'authapp/loghome.html')
