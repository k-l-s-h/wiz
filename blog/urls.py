from . import views
from django.urls import path, include
from .feeds import AtomSiteNewsFeed, LatestPostsFeed




urlpatterns = [
   
    path('Discord/', views.DiscordView.as_view(), name='Discord'),
    path('Donate/', views.DonateView.as_view(), name='Donate'),
    path('join_us/', views.join_usView.as_view(), name='join_us'),
     path('signup/', views.SignView.as_view(), name='signup'),
    path('Blog/', views.BlogView.as_view(), name='Blog'),
  
  # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'), 
   path("<slug:slug>/", views.post_detail, name="post_detail"),


   path('', views.PostList.as_view(), name='home'),
   path("feed/rss", LatestPostsFeed(), name="post_feed"),
   path("feed/atom", AtomSiteNewsFeed()),
 
  
]