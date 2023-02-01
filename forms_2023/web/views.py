from django.shortcuts import render
from forms_2023.web.forms import NameForm, PersonCreateForm
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


def index_modelform(request):
    if request.method == 'GET':
        form = PersonCreateForm()
    else:
        form = PersonCreateForm(request.POST)
        if form.is_valid():
            form.save()
            # pets = form.cleaned_data.pop('pets')
            # person = Person.objects.create(
            #     **form.cleaned_data
            # )
            # person.pets.set(pets)
            # person.save()
    context = {
        'form': form,
    }

    return render(request, 'model_forms.html', context)
