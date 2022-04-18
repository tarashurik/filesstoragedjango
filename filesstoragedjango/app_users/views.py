# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from django.contrib.auth.views import LoginView, LogoutView
# from django.views import View
# from django.contrib.auth.models import User
# from django.contrib.auth.models import Group
# from django.contrib.auth.mixins import LoginRequiredMixin
#
# from app_users.forms import RegisterForm
# from app_users.models import Profile
#
#
# class LoginUserView(LoginView):
#     template_name = 'app_users/login.html'
#
#
# class LogoutUserView(LogoutView):
#     next_page = '/'
#
#
# class RegisterView(View):
#     def get(self, request):
#         form = RegisterForm()
#         return render(request, 'app_users/register.html', context={'form': form})
#
#     def post(self, request):
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save(commit=False)
#             username = form.cleaned_data.get('username')
#             row_password = form.cleaned_data.get('password1')
#             first_name = form.cleaned_data.get('first_name')
#             last_name = form.cleaned_data.get('last_name')
#             user = User.objects.create_user(username=username, password=row_password,
#                                             first_name=first_name, last_name=last_name)
#             profile = Profile.objects.create(
#                 user=user,
#                 tel=form.cleaned_data.get('tel'),
#                 city=form.cleaned_data.get('city'),
#             )
#             group = Group.objects.get(name='regular_users')
#             group.user_set.add(user)
#             login(request, user)
#             return redirect('/')
#
#         return render(request, 'app_users/register.html', context={'form': form})
#
#
# class AccountView(LoginRequiredMixin, View):
#     def get(self, request):
#         for group in Group.objects.all():
#             if request.user in group.user_set.all():
#                 return render(request, 'app_users/account.html', {'group': group})
#         return render(request, 'app_users/account.html', {})
