from datetime import datetime, timedelta
import logging
from django.core.mail import send_mail
from config import settings
from email_distribution.models import EmailSubscribtion, EmailSubscribtionLogs
from config.settings import DEBUG


class SendEmail:
    def __init__(self, reciever, email_template) -> None:
        self.reciever_email = reciever.email
        self.reciever_fullname = reciever.full_name

        self.email_subject = email_template.email_subject
        self.email_body = email_template.email_body

        self.email_subject = self.email_subject.replace(
            '@client_fullname', self.reciever_fullname)
        self.email_subject = self.email_subject.replace(
            '@client_email', self.reciever_email)

        self.email_body = self.email_body.replace(
            '@client_fullname', self.reciever_fullname)
        self.email_body = self.email_body.replace(
            '@client_email', self.reciever_email)

    def send_email(self):
        return send_mail(
            self.email_subject,
            self.email_body,
            settings.EMAIL_HOST_USER,
            [self.reciever_email]
        )


def start_distribution_task():

    if DEBUG:
        from os.path import dirname, abspath, join
        current_path = dirname(abspath(__file__))
        logging.basicConfig(level=logging.INFO,
                            filename=join(current_path, "send_mails_log.log"),
                            filemode="w",
                            format="%(asctime)s %(levelname)s %(message)s")

    try:
        list_of_distributions = EmailSubscribtion.objects.filter(
            is_enabled='enabled',  # Рассылка включена
            status='idle',  # Не в работе
            # Дата следующей отправки меньше текущей даты
            next_send_date__lte=datetime.now(),
            time__lte=datetime.now().time()  # Время отправки меньше текущего времени
        )
        logging.info("Список рассылок")
        logging.info(list_of_distributions)

        for distribution in list_of_distributions:
            distribution.status = 'in_progress'
            distribution.save()

            sending_result = SendEmail(distribution.client,
                                       distribution.email_filling).send_email()

            if sending_result:
                match distribution.periodic_time:
                    case 'daily':
                        delta = timedelta(1)
                    case 'weekly':
                        delta = timedelta(7)
                    case 'monthly':
                        delta = timedelta(30)
                distribution.next_send_date = distribution.next_send_date + delta

            log = EmailSubscribtionLogs()
            log.subscription = distribution
            log.last_try_date = datetime.now()
            log.is_success = bool(sending_result)
            if sending_result:
                log.last_mail_response = 'success'
            else:
                log.last_mail_response = 'failure'
            log.save()

            distribution.status = 'idle'
            distribution.save()
    except Exception as e:
        logging.critical(e, exc_info=True)
