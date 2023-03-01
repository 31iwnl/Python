from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView, DeleteView

from .models import Artslice
from .forms import ArtsliceForm


def index(request):
    return render(request, 'main/index.html')


def info(request):
    ggg = Artslice.objects.all()
    fff = []
    for i in ggg:
        fff.append(i.group)
    f = '"' + '", & group="'.join(fff) + '"'
    b = '1'
    fio = request.POST.get('fio')
    idx = request.POST.get('id')
    grp = request.POST.get('grp')
    if request.POST.get('fio'):
        b = fio
    if request.POST.get('id'):
        b = idx
    if request.POST.get('grp'):
        b = grp
    if b == '1':
        g = '-group'
        h = 'ИВТ'
    elif b == '2':
        g = "full_name"
        h = 'ИВТ'
    elif b == '3':
        g = "id"
        h = 'ИВТ'
    elif b == '4':
        g = "id"
        h = 'ИВТАПбд-21'
    db = Artslice.objects.all().order_by(g).filter(group__startswith=h)
    return render(request, 'main/info.html', {'db': db})


def add(request):
    err = ''
    if request.method == 'POST':
        form = ArtsliceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info')
        else:
            err = 'Неправильно введены данные'
    form = ArtsliceForm()
    data = {
        'form': form,
        'err': err
    }
    return render(request, 'main/add.html', data)


class redact(UpdateView):
    model = Artslice
    template_name = 'main/add.html'
    fields = ['id', 'full_name', 'email', 'group']


def delete(request, pk):

    get_article = Artslice.objects.get(pk=pk)
    get_article.delete()
    return redirect(reverse('info'))
