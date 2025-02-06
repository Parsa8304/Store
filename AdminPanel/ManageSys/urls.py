from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #Done
    path('' , views.products , name = 'products' ),
    path('new', views.new_product , name = 'new-product' ) ,
    path('details/<int:product_id>', views.product_detail , name = 'product-detail' ),
    path('delete/<int:product_id>', views.delete_product, name='delete_product'),


    #Not-Done yet
    path('edit/<int:product_id>', views.edit_product , name = 'edit_product' ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


  # Check the output
