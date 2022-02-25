from typing import ItemsView
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from thingcostapi.views import register_user, login_user, UserView, DifficultyView, ResourcesView, TipsView, TypeView, ItemView, NotesView, UserPostCommentsView, UserPostView, RankingView, UserResourcesView, UserTipsView, UserTypeView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserView, 'user')
router.register(r'moneyresources', ResourcesView, 'resources')
router.register(r'difficulty', DifficultyView, 'difficulty')
router.register(r'itemtypes', TypeView, 'type')
router.register(r'tipandtricks', TipsView, 'tip')
router.register(r'usertips', UserTipsView, 'usertip')
router.register(r'userposts', UserPostView, 'userposts')
router.register(r'userpostscomments', UserPostCommentsView, 'userpostscomments')
router.register(r'userresources', UserResourcesView, 'userresources')
router.register(r'usertypes', UserTypeView, 'usertypes')
router.register(r'userranking', RankingView, 'userranking')
router.register(r'usernotes', NotesView, 'usernotes')
router.register(r'items', ItemView, 'item')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]