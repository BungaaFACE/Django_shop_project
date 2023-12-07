import random
from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint
from blog.models import BlogEntry
from email_distribution.models import Client, EmailSubscribtion
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


def index(request):
    page_data = dict()

    page_data['sub_sum'] = EmailSubscribtion.objects.count()
    page_data['active_sub_sum'] = EmailSubscribtion.objects.filter(
        is_enabled='enabled').count()
    page_data['client_sum'] = Client.objects.count()

    # Get 3 random blog entries
    blogentries_pk = list(BlogEntry.objects.filter(
        is_published=True).values_list('pk', flat=True))
    if len(blogentries_pk) <= 3:
        page_data['blog_entries'] = BlogEntry.objects.filter(is_published=True)
    else:
        random.shuffle(blogentries_pk)
        page_data['blog_entries'] = BlogEntry.objects.\
            filter(is_published=True, pk__in=blogentries_pk[:3])

    return render(request, 'main/index.html', page_data)


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
