from django.shortcuts import render,redirect,get_object_or_404
from .models import Input
from .form import ImageForm


def data(request):
    if request.method == "POST":
        image = request.FILES.get('image')
        text = request.POST.get('text', '')

        inp = Input(image=image, text= text)
        inp.save()

        id1 = inp.pk
        fil = Input.objects.filter(pk=id1)

        return render(request,'data/success.html', {'fil':fil})

    else:
        inp = Input()
    return render(request, 'data/home.html', {'inp':inp})

