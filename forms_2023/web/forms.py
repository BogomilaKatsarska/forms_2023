from django import forms

from forms_2023.web.models import Person


class NameForm(forms.Form):
    OCCUPANCIES = (
        (1, 'Child'),
        (2, 'High school student'),
        (3, 'Student'),
        (4, 'Adult'),
    )
    your_name = forms.CharField(
        label='Your name',
        max_length=50,
        help_text='Enter your name',
    )
    age = forms.IntegerField(
        label='Your age',
        initial=0,
        help_text='Enter your age',
    )
    comment = forms.CharField(
        widget=forms.Textarea,
    )
    email = forms.CharField(
        widget=forms.EmailInput(),
    )
    url = forms.CharField(
        widget=forms.URLInput(),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )
    occupancy_radio = forms.ChoiceField(
        choices=OCCUPANCIES,
        widget=forms.RadioSelect,
    )
    occupancy_select = forms.ChoiceField(
        choices=OCCUPANCIES,
    )


class PersonCreateForm(forms.ModelForm):
    story = forms.CharField(
        widget=forms.Textarea(),
    )

    class Meta:
        model = Person
        fields = '__all__'
#       fields = ('name', 'age')
#       exclude = ('pets',)
