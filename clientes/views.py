from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'persons_list.html', {'persons': persons})


@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('persons_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('persons_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    # se a requisição for do tipo POST, deletamos o objeto do banco e
    # redirecionamos para a página 'person_list'
    if request.method == 'POST':
        person.delete()
        return redirect('persons_list')

    # caso a requisição não seja do tipo POST, enviamos o usuário para
    # um formulário de confirmação, que irá retornar a requisição POST e
    # entrará na condição acima
    return render(request, 'person_delete_confirm.html', {'person': person})
