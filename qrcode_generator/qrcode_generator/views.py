from django.shortcuts import render
from django.http import HttpResponseRedirect
# from qrcode import *
import qrcode
from MyQR import myqr as mq


def home(request):
    data = "http://localhost:8000/redirect"
    qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)
    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'black',
                    back_color = 'white')
    img.save('static/image/test.png')
    return render(request, "home.html", {'data': data})



def redirect(request):
    return HttpResponseRedirect("http://google.com")

# 9491105595