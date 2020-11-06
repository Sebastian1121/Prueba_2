from django.urls import path 
from . import views

urlpatterns=[
    path('',views.index,name='index'),
  path('juego/<int:pk>', views.JuegoDetailView.as_view(), name='juego-detail'),

]



urlpatterns += [

]


'''
# Add URLConf for librarian to renew a book.
urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]


urlpatterns += [   
    path(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]
'''