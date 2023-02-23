from django.forms import ModelForm

from .models import Feedback, Subscriptions


class SubscriptionViewForm(ModelForm):
    class Meta:
        model = Subscriptions
        fields = ('name_group', 'name', 'phone', 'connection')

    def __init__(self, *args, **kwargs):
        super(SubscriptionViewForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs \
            .update({
            'placeholder': 'Введите ваше Имя',
            'class': 'input-calss_name'
        })
        self.fields['phone'].widget.attrs \
            .update({
            'placeholder': 'Введите ваш телефон',
            'class': 'input-calss_name'
        })



class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'message')

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs\
            .update({
                'placeholder': 'Введите ваш E-mail',
                'class': 'input-calss_name'
            })
        self.fields['name'].widget.attrs\
            .update({
                'placeholder': 'Введите ваше имя',
                'class': 'input-calss_name'
            })
        self.fields['message'].widget.attrs\
            .update({
                'placeholder': 'Напишите свой отзыв о нашем клубе',
                'class': 'input-calss_name'
            })
