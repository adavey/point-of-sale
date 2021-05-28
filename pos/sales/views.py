from django.shortcuts import render

# Create your views here.
from sales.models import Customer, Item, MembershipType

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_customers = Customer.objects.all().count()
    num_items = Item.objects.all().count()

    context = {
        'num_customers': num_customers,
        'num_items': num_items,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class CustomerListView(generic.ListView):
    model = Customer

class CustomerDetailView(generic.DetailView):
    model = Customer