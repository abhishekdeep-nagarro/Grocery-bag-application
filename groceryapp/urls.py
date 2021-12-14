
from django.contrib import admin
from django.urls import path
from groceryapp import views

urlpatterns = [
    path('',views.index,name='home'),
    path('add',views.add),
    path('update-list/<int:id>', views.update_list, name="update-list"),
    path('login/',views.login,name='login'),
    path('Signup',views.signup),
    path('logout/',views.signout),
    path('delete-list/<int:id>', views.delete_list),

]
