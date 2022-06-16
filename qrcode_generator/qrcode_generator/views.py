from django.shortcuts import render
from qrcode import *
data = None


def home(request):
    # global data

    # data = 'https://google.com'
    # img = make(data)
    # img.save("static/image/test.png")
    img = make('test text')
    # <class 'qrcode.image.pil.PilImage'>
    # (290, 290)

    img.save('static/image/qrcode_test.png')

    return render(request, "home.html", {'data': data})
