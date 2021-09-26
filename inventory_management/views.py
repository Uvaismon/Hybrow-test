from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Location, Product, ProductMovement, Stock

# Create your views here.

class ProductPage(ListView):
    template_name = 'inventory_management/product.html'
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Products'
        return context

class NewProduct(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')
    template_name = 'inventory_management/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New product'
        context['form_title'] = 'New Product'
        return context

class EditProduct(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')
    template_name = 'inventory_management/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit product'
        context['form_title'] = 'Edit Product'
        return context

class DeleteProduct(DeleteView):
    model = Product
    success_url = reverse_lazy('products')
    template_name = 'inventory_management/create.html'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class LocationPage(ListView):
    template_name = 'inventory_management/location.html'
    model = Location

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Locations'
        return context

class NewLocation(CreateView):
    model = Location
    fields = '__all__'
    success_url = reverse_lazy('locations')
    template_name = 'inventory_management/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Location'
        context['form_title'] = 'New Location'
        return context

class EditLocation(UpdateView):
    model = Location
    success_url = reverse_lazy('locations')
    template_name = 'inventory_management/create.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit location'
        context['form_title'] = 'Edit Location'
        return context

class DeleteLocation(DeleteView):
    model = Location
    success_url = reverse_lazy('locations')
    template_name = 'inventory_management/create.html'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class MovementPage(ListView):
    template_name = 'inventory_management/movement.html'
    model = ProductMovement

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Movements'
        return context

class NewMovement(CreateView):
    model = ProductMovement
    fields = '__all__'
    success_url = reverse_lazy('movements')
    template_name = 'inventory_management/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New movements'
        context['form_title'] = 'New Product Movement'
        return context

class EditMovement(UpdateView):
    model = ProductMovement
    success_url = reverse_lazy('movements')
    template_name = 'inventory_management/create.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit movements'
        context['form_title'] = 'Edit Product Movements'
        return context

class DeleteMovement(DeleteView):
    model = ProductMovement
    success_url = reverse_lazy('movements')
    template_name = 'inventory_management/create.html'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class Summary(ListView):
    template_name = 'inventory_management/summary.html'
    model = Stock

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Summary'
        return context

class Home(TemplateView):
    template_name = 'inventory_management/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context