import random
import string

from django.shortcuts import render, redirect, HttpResponse

urls = {}
used_ids = []
count = [0]


def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


def index(request):
    count[0] += 1
    data = {'id': count[0]}
    if 'url' in request.POST.keys() and 'id' in request.POST.keys():
        if request.POST['id'] not in used_ids:
            used_ids.append(request.POST['id'])
            url = generate_random_string(5)
            while url in urls:
                url = generate_random_string(5)
            urls[url] = request.POST['url']
            new_url = f'http://{request.get_host()}/' + url
            data['url'] = new_url
    return render(request, 'shorten/index.html', data)


def make(request):
    if 'url' in request.GET.keys():
        url = generate_random_string(5)
        while url in urls:
            url = generate_random_string(5)
        urls[url] = request.GET['url']
        new_url = f'http://{request.get_host()}/' + url
        return HttpResponse(new_url)


def redirector(request, code):
    return redirect(urls.get(code, f'http://{request.get_host()}/'))
