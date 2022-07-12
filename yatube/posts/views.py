from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('index() — для главной страницы.')


def group_posts(request, slug):
    return HttpResponse(
        'group_posts() — для страницы,'
        'на которой будут посты, отфильтрованные по группам.')
