import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q

from .forms import RequestForm
from .models import Book, Order


class BookListView(ListView):
    model = Book
    template_name = "book_list.html"


class BookDetailsView(DetailView):
    model = Book
    template_name = "book_details.html"


class SearchResultsListView(ListView):
    model = Book
    template_name = "search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")

        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )


class CheckOutView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "checkout.html"
    login_url = "login"


class RequestBookView(LoginRequiredMixin, CreateView):
    form_class = RequestForm
    template_name = "request.html"
    success_url = reverse_lazy("request")
    login_url = "login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Thank you for your suggestion!')
        HttpResponseRedirect(self.request.path_info)

        return super().form_valid(form)


def payment_complete(request):
    body = json.loads(request.body.decode("utf-8"))
    book = Book.objects.get(id=body["BookId"])

    Order.objects.create(book=book, user=request.user)

    return JsonResponse("Payment done!", safe=False)