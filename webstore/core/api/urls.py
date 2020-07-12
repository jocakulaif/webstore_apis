from django.urls import path
from core.api.views import (ProductCreateListView,
                            ClientCreateListView, ClientDetailActionsView,
                            )

app_name = 'api'

urlpatterns = [
    path('products/', ProductCreateListView.as_view(), name='products_list'),

    path('clients/', ClientCreateListView.as_view(), name='clients_list'),
    path('client/<int:pk>/', ClientDetailActionsView.as_view(), name='client_detail'),
]