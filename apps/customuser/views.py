from django.shortcuts import render, redirect
from apps.customuser.forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def profile(request):
    profile = request.user
    if request.method == 'GET':
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cambios guardados correctamente!')
        return redirect('profile')
    return render(request, 'account/profile.html', {'form': form})
