from django import forms
from character.models import Character
from character.names import get_first_name
from django.utils.safestring import mark_safe


class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    """renders horizontal radio buttons.
    found here:
    https://wikis.utexas.edu/display/~bm6432/Django-Modifying+RadioSelect+Widget+to+have+horizontal+buttons
    """
    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class UserCharacterSelectionForm(forms.ModelForm):
    """Customer = forms.ChoiceField(label=u'character_class')

    def __init__(self, *args, **kwargs):
        super(UserCharacterSelectionForm, self).__init__(*args, **kwargs)
        self.fields['Customer'].choices = [(e.id, e.Customer) for e in Character.objects.all()]"""

    print('init')

    class Meta:
        print('here')
        model = Character
        fields = ("name", "character_class")
        random_name = get_first_name()

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your characters Name', 'required': True,
                       'value': random_name}),
            'character_class': forms.RadioSelect(renderer=HorizontalRadioRenderer),
        }
