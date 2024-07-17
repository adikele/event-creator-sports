from django.shortcuts import render

# Create your views here.
from .models import Event, EventInstance, Genre, Creator

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Event.objects.all().count()
    num_instances = EventInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = EventInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Creator.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class EventListView(generic.ListView):
    model = Event

'''
example of modification:
class BookListView(generic.ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
'''