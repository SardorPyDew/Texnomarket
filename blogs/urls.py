from django.urls import path

from blogs.views import BlogListView, BlogDetailView, BlogCommentView

app_name = 'blogs'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('comment/<int:pk>/', BlogCommentView.as_view(), name='comment'),
]