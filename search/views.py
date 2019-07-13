from django.shortcuts import render

from django.db.models import Q
from movies.models import Movie


def movie_filter(request):
    if request.method == 'GET':
        q = request.GET.get('search')
        quer = Movie.objects.all()
        quer = quer.filter(Q(title__icontains=q)|Q(content__icontains=q))
        if quer != None:
            response = render(request,'movie_search.html',{'search_movie':quer,'q':q})
            return response
