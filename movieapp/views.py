from django.shortcuts import render
import requests
import json
from .forms import SearchForm

my_id = '86d4fbc5882e2f24c36bc950649e6a52'
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        searchword = request.POST.get('search')
        if form.is_valid():
            url = 'https://api.themoviedb.org/3/search/movie?api_key=' + my_id + '&query' + searchword
            response = request.get(url)
            resdata = response.text
            obj = json.loads(resdata)
            obj = obj['results']
            return render(request,'search.html', {'resdata':resdata})
        # 입력된 내용을 바탕으로
        # https://api.themoviedb.org/3/search/movie?api_key=86d4fbc5882e2f24c36bc950649e6a52&language=en-US&query=hello&page=1&include_adult=false
        # 위형태 url로 get 요청
    else:
        form = SearchForm()
        url = 'https://api.themoviedb.org/3/trending/movie/week?api_key=' + my_id
        response = requests.get(url)
        resdata = response.text
        obj = json.loads(resdata)
        obj = obj['results']

    return render(request, 'index.html', {'obj':obj, 'form':form})

def detail(request, movie_id):
    url = 'https://api.themoviedb.org/3/movie/' + movie_id + '?api_key=' + my_id
    response = requests.get(url)
    resdata = response.text
    return render(request, 'detail.html', {"resdata":resdata})