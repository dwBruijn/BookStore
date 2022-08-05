from django.urls import path

from .views import BookListView, BookDetailsView, CheckOutView, payment_complete, SearchResultsListView, RequestBookView

urlpatterns = [
    path("", BookListView.as_view(), name="list"),
    path("<int:pk>/", BookDetailsView.as_view(), name="details"),
    path("<int:pk>/checkout/", CheckOutView.as_view(), name="checkout"),
    path("complete/", payment_complete, name="complete"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
    path("request/", RequestBookView.as_view(), name="request"),
]