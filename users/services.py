from django.core.mail import send_mail
from config import settings
from django.urls import reverse


def send_verification_code(request):
    url = reverse('verify_email_link', args=[
                  request.user.email_verification_token])
    full_url = request.build_absolute_uri(url)

    send_mail(
        'Подтверждение почты bungaa-shop',
        f'Для подтверждения вашей почты введите код на странице подтверждения: {full_url}',
        settings.EMAIL_HOST_USER,
        [request.user.email]
    )
