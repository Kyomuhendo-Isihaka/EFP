from django.contrib import admin
from django.urls import path
from efp_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.efarm, name='efarm'),
    path('registration', views.registration, name='registration'),
    path('all_categories',views.all_categories, name='all-categories'),
    path('all_products',views.all_products, name='all-products'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('login/<str:role>/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard/<str:role>/<int:user_id>', views.dashboard, name="dashboard"),

    path('products/<str:role>/<int:user_id>', views.products, name="products"),
    path('products/<str:role>/<int:user_id>/<int:pk>/', views.products, name='edit_product'),
    path('product_details/<int:pk>', views.product_details, name="product_details"),
    path('delete_product/<str:role>/<int:user_id>/<int:pk>', views.delete_product, name="delete_product"),

    path('categories/<str:role>/<int:user_id>', views.categories, name="categories"),
    path('categories/<str:role>/<int:user_id>/<int:pk>/', views.categories, name='edit_category'),
    path('delete_category/<str:role>/<int:user_id>/<int:pk>', views.delete_category, name="delete_category"),
    path('category_products/<int:categoryID>', views.category_products, name="category_products"),
    
    path('farmers/<str:role>/<int:user_id>', views.farmers, name="farmers"),
    path('customers/<str:role>/<int:user_id>', views.customers, name="customers")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
