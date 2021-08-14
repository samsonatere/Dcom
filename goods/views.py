from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from store.models import Product

class DetailView(DetailView):
    model = Product
    template_name = 'detail.html'

class UpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ('name', 'price', 'image')
    template_name = 'edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.poster == self.request.user

class DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'delete.html'
    success_url = reverse_lazy('store')

    def test_func(self):
        obj = self.get_object()
        return obj.poster == self.request.user

class CreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'new.html'
    fields = ('name', 'price', 'digital', 'image')

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)