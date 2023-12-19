from django.shortcuts import render


def Index(request):


    return render(request, 'index.html')



def Home(request):


    return render(request, 'home.html')


def Brothers(request):

    return render(request, 'brothers.html')

def Gardens(request):

    return render(request, 'gardens.html')

def Retreat(request):

    return render(request, 'retreat.html')

def WeAre(request):

    return render(request, 'who-we-are.html')

def Grounds(request):

    return render(request, 'grounds-tour.html')

def DailyLife(request):


    return render(request, 'daily-life.html')

def Vacations(request):

    return render(request, 'vacations.html')

def PrayWithUs(request):

    return render(request, 'pray-with-us.html')

def Support(request):

    return render(request, 'support.html')

def LadyOfMepkin(request):

    return render(request, 'lady-of-mepkin.html')

def VirtualTour(request):

    return render(request, 'virtual-tour.html')

def LaurensCemetry(request):

    return render(request, 'laurens-cemetry.html')

