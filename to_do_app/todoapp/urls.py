from django.urls import path
from .views import delete, home, cross_off, uncross, edit

urlpatterns = [
    path('', home, name='home'),
    path('delete/<TodoListItem_id>', delete, name='delete'),
    path('cross_off/<TodoListItem_id>', cross_off, name='cross_off'),
    path('uncross/<TodoListItem_id>', uncross, name='uncross'),
    path('edit/<TodoListItem_id>', edit, name='edit'),
]
