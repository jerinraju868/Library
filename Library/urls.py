from django.urls import path

from Library import  views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('books/', views.BookList.as_view(), name='books'),
    path('authors/',views.AuthorList.as_view(), name='authors'),
    path('create/',views.CreateBook.as_view(), name='book_create'),
    path('detail/<int:pk>/',views.ViewBook.as_view(), name='book_detail'),
    path('update/<int:pk>/', views.UpdateBook.as_view(),name='book_update'),
    path('delete/<int:pk>/', views.DeleteBook.as_view(),name='book_delete'),
]