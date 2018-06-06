from __future__ import unicode_literals
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .forms import SignUpForm
from .tokens import account_activation_token
from django.shortcuts import render
from .models import Profile
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import logout as original_logout
from django.contrib.auth.views import login as original_login
from django.contrib.sessions.backends.base import SessionBase


 
class ProfileList(LoginRequiredMixin,ListView):
    template_name = 'home.html'
    model = Profile

@login_required
def home(request):
    return render(request, 'home.html')

def alt_logout(request, *args, **kwargs):
    for sesskey in request.session.keys():
        del request.session[sesskey]
    return original_logout(request, *args, **kwargs)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('users/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            return redirect('account_activation_sent') 
    else:
        form = SignUpForm()
    return render(request, 'users/registration.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'users/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'users/account_activation_invalid.html')







# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
# from django.contrib.auth import update_session_auth_hash, login, authenticate
# from django.contrib import messages
# from django.shortcuts import render, redirect

# from social_django.models import UserSocialAuth

# def signup(request):
#     print current_user.id
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = authenticate(
#                 username=form.cleaned_data.get('username'),
#                 password=form.cleaned_data.get('password1')
#             )
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/registration.html', {'form': form})

# @login_required
# def home(request):
#     return render(request, 'users/home.html')

# @login_required
# def settings(request):
#     user = request.user

#     try:
#         github_login = user.social_auth.get(provider='github')
#     except UserSocialAuth.DoesNotExist:
#         github_login = None
#     try:
#         twitter_login = user.social_auth.get(provider='twitter')
#     except UserSocialAuth.DoesNotExist:
#         twitter_login = None
#     try:
#         facebook_login = user.social_auth.get(provider='facebook')
#     except UserSocialAuth.DoesNotExist:
#         facebook_login = None

#     can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

#     return render(request, 'core/settings.html', {
#         'github_login': github_login,
#         'twitter_login': twitter_login,
#         'facebook_login': facebook_login,
#         'can_disconnect': can_disconnect
#     })

# @login_required
# def password(request):
#     if request.user.has_usable_password():
#         PasswordForm = PasswordChangeForm
#     else:
#         PasswordForm = AdminPasswordChangeForm

#     if request.method == 'POST':
#         form = PasswordForm(request.user, request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('password')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordForm(request.user)
#     return render(request, 'core/password.html', {'form': form})
