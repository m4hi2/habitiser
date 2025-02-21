from django.shortcuts import redirect, render

from users.forms import CustomUserCreationForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, "users/register.html", {"form": form})

    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})
