import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from .models import UrlData
from .forms import Url


def generate_slug():
    return ''.join(
        random.choices(string.ascii_letters + string.digits, k=10)
    )


def urlShort(request):
    form = Url(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        original_url = form.cleaned_data['url']

        slug = generate_slug()
        while UrlData.objects.filter(slug=slug).exists():
            slug = generate_slug()

        UrlData.objects.create(url=original_url, slug=slug)
        return redirect('/')

    data = UrlData.objects.all()
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'index.html', context)


def urlRedirect(request, slugs):
    data = get_object_or_404(UrlData, slug=slugs)
    return redirect(data.url)
