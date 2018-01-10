from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserRegistrationForm
from .models import Profile


@login_required
def profile(request):
    return render(request,
                  'tracker/profile.html')


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # New user object is created but not saved into database
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            # Create profile object
            profile = Profile(user=new_user)
            profile.save()

            # log in user
            login(request, new_user)

            return redirect('dashboard')

    user_form = UserRegistrationForm()
    return render(request,
                  'registration/register.html',
                  {'user_form': user_form})
