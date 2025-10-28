from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import render, redirect


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            reader = Group.objects.get(name='Reader')
            user.groups.add(reader)
            return redirect('login')
        else:
            messages.error(request, "Дані не валідні!")
    else:
        form = UserCreationForm()

    return render(request, "accounts/registration.html", {'form': form})

