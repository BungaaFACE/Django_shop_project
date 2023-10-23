from django.shortcuts import render
from django.http import HttpResponse


def test_http_response(request):
    return HttpResponse("""<h4>Привет мир!</h4><h3>Навигация</h3>
                        <ul>
                            <a href="/"><li><i class="fa-solid fa-house fa-fade"></i>Главная</li></a>
                            <a href="test_http_response"><li><i class="fa-solid fa-flask-vial fa-fade"></i>Test HttpResponse</li></a>
                            <a href="test_include"><li><i class="fa-solid fa-flask-vial fa-fade"></i>Test { %include% }</li></a>
                        </ul>""")


def test_include(request):
    return render(request, 'main/test_include.html')


def index(request):
    return render(request, 'main/index.html')


def contacts(request):
    return render(request, 'main/contacts.html')
