from django.forms import ModelForm
from django.utils.crypto import get_random_string

from hashing_app import settings
from urls_hash.models import HashedUrl


class HashUrlForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(HashUrlForm, self).__init__(*args, **kwargs)
        self.fields['hash_value'].required = False

    class Meta:
        model = HashedUrl
        fields = ['hash_value', 'url']
        required = ['url']

    def clean_hash_value(self):
        if not self.cleaned_data['hash_value']:
            self.cleaned_data['hash_value'] = get_random_string(
                length=settings.DEFAULT_HASH_LENGTH
            )

        return self.cleaned_data['hash_value']
