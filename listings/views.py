from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import color_choices, material_choices, style_choices

from .models import Listing

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }

  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
    'listing': listing
  }

  return render(request, 'listings/listing.html', context)

def search(request):
  queryset_list = Listing.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # Style
  if 'style' in request.GET:
    style = request.GET['style']
    if style:
      queryset_list = queryset_list.filter(style__iexact=style)

  # Material
  if 'material' in request.GET:
    material = request.GET['material']
    if material:
      queryset_list = queryset_list.filter(material__lte=material)

  # Color
  if 'color' in request.GET:
    color = request.GET['color']
    if color:
      queryset_list = queryset_list.filter(color__lte=color)

  context = {
    'style_choices': style_choices,
    'material_choices': material_choices,
    'color_choices': color_choices,
    'listings': queryset_list,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context)
