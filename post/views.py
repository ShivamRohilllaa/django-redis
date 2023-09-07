from django.shortcuts import render
from post.models import Post
from django.core.cache import cache
from django.http import HttpResponse

# Create your views here.

def home(request):
    qs = Post.objects.all()
    context = {'qs':qs}
    return render(request, 'index.html', context)

def set_data_in_cache(request):
    # Retrieve the data you want to cache
    qs = Post.objects.all()

    # Set the data in the Redis cache
    cache.set('post_data_key', qs)

    return HttpResponse("Data has been set in the cache.")

def get_data_from_cache(request):
    # Get the data from the Redis cache
    cached_data = cache.get('post_data_key')
    print(cached_data, 'cached_data')

    if cached_data is not None:
        # If data is found in the cache, you can use it as needed
        return render(request, 'redis_data.html', {'qs': cached_data})
    else:
        # If data is not found in the cache, you may choose to retrieve it from the database
        qs = Post.objects.all()
        return render(request, 'index.html', {'qs': qs})

