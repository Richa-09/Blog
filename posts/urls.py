from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('show/',views.show,name='show'),
    path('create/',views.create,name='create'),
    path('blog/<int:k>',views.blog,name='blog'),
    path('delete/<int:p>',views.delete,name='delete'),
    path('done/<int:k>',views.done,name='done'),
    path('comment/<int:p>',views.commentpage,name='comment'),
    path('add_comment/<int:p>',views.add_comment,name='add_comment'),
]