from .models import checkout
from django.shortcuts import render
from .models import checkout
from django.http import FileResponse
from django.core.paginator import Paginator
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'recognize.html')

def contact(request):
    return render(request, 'Contact.html')

def ITGO(request):
    return render(request, 'ITGO.html')

def ITGOContact(request):
    return render(request, 'ITGOContact.html')

def ITGOGames(request):
    return render(request, 'ITGOGames.html')

def ITGOGContact(request):
    return render(request, 'ITGOGamesContact.html')

def ITGOabout(request):
    return render(request, 'aboutITGO.html')

def zakaz(request):
    return render(request, 'Zakaz.html')
def AGOG(request):
    return render(request, 'aboatITGOG.html')

def allGame(request):
    return render(request, 'UZNGAME.html')

def DownloadLiam(request):
    return render(request, 'DownloadLiam.html')

def Uzn(request):
    return render(request, 'UZN.html')


def withdrawal_notice_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        mail = request.POST.get('mail')
        
        # Создание объекта WithdrawalNotice и сохранение в базе данных
        checkout.objects.create(username=username, phone=phone, mail=mail)
        
        # Вернуть контекст с информацией об успешной отправке данных
        return render(request, 'withdrawal_notice_form.html', {'success': True})
        
    return render(request, 'withdrawal_notice_form.html')

def android_download(request):
    return FileResponse (open('APP/files/liam.history.apk','rb'), as_attachment=True)

def linux_download(request):
    return FileResponse (open('APP/files/HistoryLiam-linux.tar.bz2','rb'), as_attachment=True)

def mac_download(request):
    return FileResponse (open('APP/files/HistoryLiam-mac.zip','rb'), as_attachment=True)

def windows_download_zip(request):
    return FileResponse (open('APP/files/HistoryLiam-win.zip','rb'), as_attachment=True)

def windows_download_exe(request):
    return FileResponse (open('APP/files/Setup.exe','rb'), as_attachment=True)
