from django.urls import path
from .views import (
    phonebook_detail_view,
    phonebook_create_view,
    phonebook_update_view,
    phonebook_delete_view,
    phonebook_add_phone_number_view,
    phonebook_add_adress_email_view,
    OsobaListView,
    phonebook_list_view
    )

app_name = 'phonebook'
urlpatterns = [
    path('', phonebook_list_view, name='phonebook-list'),
    path('create/', phonebook_create_view, name='phonebook-create'),
    path('<int:id>/', phonebook_detail_view, name='phonebook-detail'),
    path('<int:id>/update/', phonebook_update_view, name='phonebook-update'),
    path('<int:id>/delete/', phonebook_delete_view, name='phonebook-delete'),
    path('<int:id>/phone/', phonebook_add_phone_number_view, name='phonebook-add-phone-number'),
    path('<int:id>/email/', phonebook_add_adress_email_view, name='phonebook-add-adress-email'),
]