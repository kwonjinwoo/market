from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect , render
from .forms import UsersForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def signup(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = UsersForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)
    

# @require_http_methods(["GET", "POST"])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get('next') or 'index'
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)

# @require_POST
def logout(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect('index')



