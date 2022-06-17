from django.http import HttpResponse


def DetailFrozeView(request):
    return HttpResponse("Страница с деталями заявки")
