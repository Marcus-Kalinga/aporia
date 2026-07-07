from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BookModel
from django import forms
from django.utils import timezone

# Create a form class based on your model
class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['book_title', 'book_author', 'book_short_review']
        labels = {
            'book_title': 'Book Title',
            'book_author': 'Author',
            'book_short_review': 'Your Review'
        }
        widgets = {
            'book_short_review': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }

def book_list(request):
    # Handle form submission
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Save the new book entry
            form.save()
            # Redirect to the same page to prevent form resubmission
            return redirect('books:book_list')
    else:
        form = BookForm()
    
    # Get all books, ordered by newest first
    books = BookModel.objects.all().order_by('-date_added')
    
    # Render the template with form and books
    context = {
        'form': form,
        'books': books,
    }
    return render(request, 'books/book_list.html', context)
