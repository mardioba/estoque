from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from .models import Produto
from .forms import ProdutoForm
from django.urls import reverse_lazy
def produto_list(request):
  template_name = 'produto_list.html'
  objects = Produto.objects.all()
  context={'object_list': objects}
  return render(request, template_name, context)

def produto_detail(request, pk):
  template_name = 'produto_detail.html'
  obj = Produto.objects.get(pk=pk)
  context={'object': obj}
  return render(request, template_name, context)

def produto_add(request):
  template_name = 'produto_form.html'
  return render(request, template_name)

class ProdutoCreate(CreateView):
  model = Produto
  template_name = 'produto_form.html'
  form_class = ProdutoForm
  # success_url = reverse_lazy('produto:produto_list')

class ProdutoUpdate(UpdateView):
  model = Produto
  template_name = 'produto_form.html'
  form_class = ProdutoForm