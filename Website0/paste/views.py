import random
import string

from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

urls = {}


def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


def index(request):
    if 'text' in request.POST.keys():
        url = generate_random_string(5)
        while url in urls:
            url = generate_random_string(5)
        urls[url] = request.POST['text'].split('\n')
        return redirect(f'http://{request.get_host()}/paste/' + url)
    return render(request, 'paste/index.html', {})


@csrf_exempt
def make(request):
    if 'text' in request.POST.keys():
        url = generate_random_string(5)
        while url in urls:
            url = generate_random_string(5)
        urls[url] = [x+'\r' for x in request.POST['text'].split('\n')]
        new_url = f'http://{request.get_host()}/paste/' + url
        return HttpResponse(new_url)


def redirector(request, code):
    return render(request, 'paste/template.html', {'data': urls.get(code)})
