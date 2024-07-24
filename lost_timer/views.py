from django.shortcuts import render


def clock_view(request):
    return render(request, 'clock.html')


def console_view(request):
    return render(request, 'console.html')
