
from django.urls import path
from .views import dashboard, settings, allbookmarks

from .views import dashboard, settings, plans, upgradeComplete
from apps.marks.views import categories, category, categoryCreate, categoryUpdate,categoryDelete, bookmarkCreate, bookmarkUpdate,bookmarkDelete

from apps.marks.api import api_delete_category, api_delete_bookmark,api_increase_visits

urlpatterns = [
    # Admin panel page urls
    path('', dashboard, name='dashboard'),
    path('settings', settings, name='settings'),
    path('allbookmarks/', allbookmarks, name='allbookmarks'),



    # category urls
    path('categories/', categories, name='categories'),
    path('categories/<int:category_id>/', category, name='category'),
    path('categories/add/', categoryCreate, name='category_add'),
    path('categories/<int:category_id>/edit', categoryUpdate, name='category_edit'),
    path('categories/<int:category_id>/delete', categoryDelete, name='category_delete'),

    # bookmarks urls
    path('categories/<int:category_id>/add_bookmark/', bookmarkCreate, name='bookmark_add'),
    path('categories/<int:category_id>/edit_bookmark/<int:bookmark_id>/', bookmarkUpdate, name='bookmark_edit'),
    path('categories/<int:category_id>/delete_bookmark/<int:bookmark_id>/', bookmarkDelete, name='bookmark_delete'),

    # settings urls
    path('settings/', settings, name='settings'),
    path('settings/upgrage-plans/', plans, name='upgrage-plans'),
    path('settings/upgradeComplete/', upgradeComplete, name='upgradeComplete'),

    #apis
    path('api/delete_category/<int:category_id>/', api_delete_category, name='api_delete_category'),
    path('api/delete_bookmark/<int:bookmark_id>/', api_delete_bookmark, name='api_delete_bookmark'),
    path('api/increase_visits/<int:bookmark_id>/', api_increase_visits, name='api_increase_visits'),

    # Admin panel apis
]
