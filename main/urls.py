from django.urls import path
from main.views import show_main, create_product_entry, show_xml,show_json, show_xml_by_id, show_json_by_id
from . import views
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_product
from main.views import delete_product
app_name = 'main'

urlpatterns = [
    path ('', views.show_main, name='show_main'),
    path ('create_product_entry', create_product_entry, name='create_product_entry'),
    path ('xml/', show_xml, name='show_xml'),
    path ('json/', show_json, name='show_json'),
    path ('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path ('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path ('register/', register, name='register'),
    path ('login/', login_user, name='login'),
    path ('logout/', logout_user, name='logout'),
    path ('edit_product/<uuid:id>/', edit_product, name='edit_product'),
    path ('delete_product/<uuid:id>/', delete_product, name='delete_product'),
]