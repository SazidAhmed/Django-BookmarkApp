from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Category, Bookmark
from .forms import CategoryForm, BookmarkForm

@login_required
def categories(request):
  categories = request.user.categories.all()
  context={
    'categories':categories
  }
  return render(request, 'marks/categories.html', context)

@login_required
def category(request, category_id):
  category = Category.objects.get(pk=category_id)
  bookmarksstring = ''

  for bookmark in category.bookmarks.all():
    editurl = reverse('bookmark_edit', args=[category.id, bookmark.id])
    b = "{'id': '%s', 'title': '%s', 'description': '%s', 'url': '%s', 'editurl': '%s', 'visits': '%s'}," % (bookmark.id, bookmark.title, bookmark.description, bookmark.url,  editurl, bookmark.visits)

    bookmarksstring = bookmarksstring + b
  # print(bookmarksstring)
  context = {
    'category':category,
    'bookmarksstring':bookmarksstring
  }
  return render(request, 'marks/category.html', context)

@login_required
def categoryCreate(request):
  canAdd = ''
  # count the number of user categories
  categories = request.user.categories.all().count()

  if categories >= 10 and request.user.userprofile.plan == 'pro':
    canAdd = 'You can\'t have more than 10 categories when you\'re on the Pro plan!'

  if categories >= 5 and not request.user.userprofile.plan == 'pro':
    canAdd = 'You can\'t have more than 5 categories when you\'re on the Basic plan!'

  # Post data 
  if request.method == 'POST':
    form = CategoryForm(request.POST)

    if form.is_valid():
      try:
        category = form.save(commit=False)
        category.created_by = request.user
        category.save()
        messages.success(request, 'The category has been added!')
        return redirect('categories')
      except:
        pass
    else:
      return redirect(request,'marks/category_form.html', {'form':form, 'canAdd':canAdd})
  else:
    form = CategoryForm(request.POST)
    return render(request,'marks/category_form.html', {'form':form, 'canAdd':canAdd})

@login_required
def categoryUpdate(request, category_id):
  category = Category.objects.filter(created_by=request.user).get(pk=category_id)

  if request.method == 'POST':
    form = CategoryForm(request.POST, instance=category)

    if form.is_valid():
      form.save()
      messages.success(request, 'The category has been updated!')
      return redirect('categories')
  else:
    form = CategoryForm(instance=category)
    context={'form':form, 'category':category}
    return render(request,'marks/category_edit.html', context)

@login_required
def categoryDelete(request, category_id):
  category = Category.objects.filter(created_by=request.user).get(pk=category_id)
  category.delete()
  messages.success(request, 'The category has been deleted!')
  return redirect('categories')

# bookmarks
@login_required
def bookmarkCreate(request, category_id):
  canAdd = ''
  # count the number of user bookmarks
  bookmarks = request.user.bookmarks.all().count()

  # if bookmarks >= 50 and request.user.userprofile.plan == 'pro':
  if bookmarks >= 50 and not request.user.userprofile.plan == 'pro':
    canAdd = 'You can\'t have more than 50 bookmarks when you\'re on the Pro plan!'

  if bookmarks >= 20 and request.user.userprofile.plan == 'basic':
    canAdd = 'You can\'t have more than 20 bookmarks when you\'re on the Basic plan!'

  # form 
  if request.method == 'POST':
    form = BookmarkForm(request.POST)

    if form.is_valid():
      try:
        bookmark = form.save(commit=False)
        bookmark.created_by = request.user
        bookmark.category_id = category_id
        bookmark.save()
        messages.success(request, 'The Bookmark has been added!')
        return redirect('category', category_id=category_id)
      except:
        pass
    else:
      return redirect(request,'marks/bookmark_form.html', {'form':form, 'canAdd':canAdd})
  else:
    form = BookmarkForm(request.POST)
    return render(request,'marks/bookmark_form.html', {'form':form, 'canAdd':canAdd})

@login_required
def bookmarkUpdate(request, category_id, bookmark_id):
  bookmark = Bookmark.objects.filter(created_by=request.user).get(pk=bookmark_id)
  if request.method == 'POST':
    form = BookmarkForm(request.POST, instance=bookmark)

    if form.is_valid():
      form.save()
      messages.success(request, 'The Bookmark has been updated!')
      return redirect('category', category_id=category_id)
  else:
    form = BookmarkForm(instance=bookmark)
    context={'form':form, 'bookmark':bookmark}
    return render(request,'marks/bookmark_edit.html', context)

@login_required
def bookmarkDelete(request, category_id, bookmark_id):
  bookmark = Bookmark.objects.filter(created_by=request.user).get(pk=bookmark_id)
  bookmark.delete()
  messages.success(request, 'The Bookmark has been deleted!')
  return redirect('category', category_id=category_id)