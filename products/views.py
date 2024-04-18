from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from .models import Products

@require_POST
def delete(request, pk):
    if request.method == "POST":
        product = Products.objects.get(pk=pk)
        product.delete()
        return redirect("index")
    return redirect("products:detail", pk)



def index(request):
    products = Products.objects.all()
    context = {
        'products': products,
    }
    return render(request, "products/index.html" ,context)


def detail(request, pk):
    product = Products.objects.get(pk=pk)
    context = {
        'product': product,
    }
    return render(request, "products/detail.html" ,context)

@require_http_methods(["GET", "POST"])
def update(request, pk):
    product = Products.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect('products:detail', product.pk)
    else:
        form = PostForm(instance=product)
        context = {
            'form': form,
            'product': product,
        }
    return render(request, 'products/update.html', context)

# @login_required
def new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # post = form.save(commit=False)
            # post.user = request.user
            form.save()
            return redirect("index")
    else:
        form = PostForm()
    context = {"form": form}
    return render(request, "products/newposts.html", context)