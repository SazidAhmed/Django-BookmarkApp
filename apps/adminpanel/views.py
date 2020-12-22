import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

from apps.marks.models import Bookmark, Category
from apps.userprofile.models import Userprofile

@login_required
def dashboard(request):
  categories = request.user.categories.all().order_by('-created_at')[0:5]
  bookmarks = request.user.bookmarks.all().order_by('-created_at')[0:5]
  context={'bookmarks':bookmarks, 'categories':categories}
  return render(request, 'dashboard.html', context)

@login_required
def allbookmarks(request):
  bookmarks = request.user.bookmarks.all().order_by('-created_at')
  context={'bookmarks':bookmarks}
  return render(request, 'allbookmarks.html', context)

@login_required
def settings(request):
  return render(request, 'settings.html')

@login_required
def plans(request):
  # products = Product.objects.all()
  # context={ 'products': products }
  return render(request, 'plans.html')

@login_required
def upgradeComplete(request):
  return render(request, 'upgradeComplete.html')

@login_required
def settings(request):
  if request.method == 'POST':
  #get from values
    first_name = request.POST.get('first_name', '')
    last_name = request.POST.get('last_name', '')
    username = request.POST.get('username', '')
    email = request.POST.get('email', '')
    plan = request.POST.get('plan', '')

    user = request.user

    if username != request.user.username:
      usernames = User.objects.filter(username=username)

      if len(usernames):
        messages.error(request, 'That Username Already Exist!')
        return redirect('settings')
      else:
        user.username = username

    if email != request.user.email:
      useremails = User.objects.filter(email=email)
      
      if len(useremails):
        messages.error(request, 'That Email Already Exist!')
        return redirect('settings')
      else:
        user.email = email
    else:    
      user.first_name = first_name
      user.last_name = last_name
      user.save()

      user.userprofile.plan = plan
      user.userprofile.save() 

      messages.success(request, 'Profile Has Been Updated!')
      return redirect('settings')
  else:
    return render(request, 'settings.html')

@login_required
def changePass(request):
  if request.method == 'POST':
    password = request.POST.get('password', '')
