from django import forms
from email_distribution.models import Client, EmailFilling, EmailSubscribtion


class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Client
        exclude = ('user',)


class EmailFillingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = EmailFilling
        exclude = ('user',)


class EmailSubscribtionFormAdmin(forms.ModelForm):

    class Meta:
        model = EmailSubscribtion
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].widget = forms.widgets.TimeInput(
            attrs={'type': 'time'})

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class EmailSubscribtionFormUser(EmailSubscribtionFormAdmin):

    class Meta:
        model = EmailSubscribtion
        fields = ("client", 'periodic_time', 'time',
                  'email_filling', 'is_enabled')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EmailSubscribtionFormManager(EmailSubscribtionFormUser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widgets['client'].attrs['readonly'] = ''
        self.widgets['periodic_time'].attrs['readonly'] = ''
        self.widgets['time'].attrs['readonly'] = ''
        self.widgets['email_filling'].attrs['readonly'] = ''
