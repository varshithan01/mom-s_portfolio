from django.shortcuts import render, redirect
from .models import Publication
from .forms import PublicationForm

def index(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Prevent form resubmission on reload
    else:
        form = PublicationForm()

    publications = Publication.objects.all().order_by('-id')  # newest first
    return render(request, 'portm/index.html', {
        'form': form,
        'publications': publications
    })


def publication_list(request):
    publications = Publication.objects.all()
    return render(request, 'publication_list.html', {'publications': publications})
