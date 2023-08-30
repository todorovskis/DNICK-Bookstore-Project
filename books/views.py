from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .forms import BookForm
from .models import *


def store(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'store/store.html', context)


def fill_context(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_order_total': 0, 'get_order_quantity': 0}
    context = {'items': items, 'order': order}
    return context


def cart(request):
    context = fill_context(request)
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = fill_context(request)
    return render(request, 'store/checkout.html', context)


def update_book(request, id):
    if request.method == 'GET':
        book = Book.objects.filter(id=id).first()
        context = {'book': book}
        return render(request, 'store/edit-book.html', context)

    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')

        book = Book.objects.filter(id=id).first()

        book.title = title
        new_author = Author(name=author)
        new_author.save()
        book.author = new_author
        book.description = description
        book.save()

    return view_book(request, id)


def delete_book(request, id):
    book = Book.objects.filter(id=id).first()
    book.delete()
    return store(request)


def add_book(request):
    authors = Author.objects.all()

    if request.method == "POST":
        form_data = BookForm(request.POST, request.FILES)
        if form_data.is_valid():
            title = form_data.cleaned_data['title']
            author_id = form_data.cleaned_data['author']
            description = form_data.cleaned_data['description']
            price = form_data.cleaned_data['price']

            print(author_id)
            author = Author.objects.filter(Author, id=author_id)

            book = Book.objects.create(
                title=title,
                author=author,
                description=description,
                price=price
            )
            book.save()
            return redirect("store")
        else:
            print("Form errors:", form_data.errors)
    else:
        form_data = BookForm()

    return render(request, "store/add-book.html", context={"form": form_data, "authors": authors})


def card(request):
    return render(request, 'store/card-info.html')


def register(request):
    return render(request, 'store/register.html')


def login(request):
    return render(request, 'store/login.html')


def view_book(request, id):
    book = Book.objects.filter(id=id).first()
    context = {'book': book}
    return render(request, 'store/book.html', context)
