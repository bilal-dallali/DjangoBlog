from django.http import HttpResponse


def vue_de_test(request):
    return HttpResponse("<h1>Vue de test</h1>")