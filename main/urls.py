from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import index, PostDetail, news_all, ContactView, TeamDetail, TeamAll, club, CategoryNews, Galery, subscription, \
    locations, SubscriptionView

urlpatterns = [
    path('', index, name='index'),
    path('subscription/buy/', SubscriptionView.as_view(), name='subscription'),
    path('locations/', locations, name='locations'),
    path('subscription/', subscription, name='sub'),
    path('galery/', Galery.as_view(), name='galery'),
    path('category/<str:slug>/', CategoryNews.as_view(), name='category'),
    path('club/', club, name='club'),
    path('team/', TeamAll.as_view(), name='team_all'),
    path('team_detail/<int:pk>/', TeamDetail.as_view(), name='team'),
    path('post/<str:slug>/', PostDetail.as_view(), name='detail'),
    path('news_all/', news_all, name='news_all'),
    path('contact/', ContactView.as_view(), name='contact'),
]
