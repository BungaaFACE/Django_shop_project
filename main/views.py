from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint
from main.models import Contacts


def test_http_response(request):
    return HttpResponse("""<h4>Привет мир!</h4><br>
                        <h3>Навигация</h3>
                        <ul>
                            <a href="/"><li><i class="fa-solid fa-house fa-fade"></i>Главная</li></a>
                            <a href="test_http_response"><li><i class="fa-solid fa-flask-vial fa-fade"></i>Test HttpResponse</li></a>
                            <a href="test_include"><li><i class="fa-solid fa-flask-vial fa-fade"></i>Test { %include% }</li></a>
                        </ul>""")


def test_include(request):
    return render(request, 'main/test_include.html')


def contacts(request):
    if request.method == 'POST':
        data = {}
        # в переменной request хранится информация о методе, который отправлял пользователь
        data['email'] = request.POST.get('email')
        data['mobile_number'] = request.POST.get('mobile_number')
        data['customer_needs'] = request.POST.get('customer_needs')
        # а также передается информация, которую заполнил пользователь
        pprint(data)
    feedback_data = Contacts.objects.get(id=1)

    return render(request, 'main/contacts.html', {'feedback_data': feedback_data})
