from django.urls import path
from .views import (
    HomeView,
    product,
    ItemDetailView,
    add_to_cart,
    remove_from_cart,
    OrderSummaryView,
    remove_single_item_from_cart,
    add_single_item_to_cart,
    CheckoutView,
    PaymentView,
    SearchResultsView,
    ShirtView,
    TrouserView,
    ShoeView,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/', product, name='product'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('remove-single-item-from-cart/<slug>/',
         remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('add-single-item-to-cart/<slug>/',
         add_single_item_to_cart, name='add-single-item-to-cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('shirts/', ShirtView.as_view(), name='shirts'),
    path('trousers/', TrouserView.as_view(), name='trousers'),
    path('shoes/', ShoeView.as_view(), name='shoes')
]
