from django.shortcuts import render
from forms_2023.web.forms import NameForm
from forms_2023.web.models import Person


def index(request):
    your_name = None
    if request.method == 'GET':
        form = NameForm()
    else:
        form = NameForm(request.POST)
        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            Person.objects.create(
                name=your_name,
            )
    context = {
        'form': form,
        'your_name': your_name,
    }
    return render(request, 'index.html', context)
