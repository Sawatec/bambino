from django.urls import include, path

from . import views

urlpatterns = [
    path('showUser/', views.user_list, name='userVerwaltung'),
    path('showChildren/', views.child_list, name='kinderVerwaltung'),
    path('showUser/update_user/<int:pk>', views.showUpdateUser, name='userUpdate'),
    path('showUser/delete_user/<int:pk>', views.deleteUser, name='userDelete'),
]
