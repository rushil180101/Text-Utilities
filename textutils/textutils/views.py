from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):
    text = request.POST.get('text','')
    text_copy = text
    parameters = {'purpose':'','analyzed':''}
    flag = 0

    if request.POST.get('removepunc','off') == "on":
        punctuations = '''.,:;?()[]'"!_-/`~@#$%^&*+=<>'''
        received_text = text
        analyzed = ""
        for char in received_text:
            if char not in punctuations:
                analyzed = analyzed + char
        text = analyzed
        parameters['purpose'] = "Removed Punctuations"
        parameters['analyzed'] = analyzed
        flag = 1

    if request.POST.get('uppercase','off') == "on":
        received_text = text
        analyzed = received_text.upper()
        text = analyzed
        parameters['purpose'] = "Converted to UPPER CASE"
        parameters['analyzed'] = analyzed
        flag = 1

    if request.POST.get('removeNums','off') == "on":
        received_text = text
        analyzed = ""
        numbers = "1234567890"
        for char in received_text:
            if char not in numbers:
                analyzed = analyzed + char
        text = analyzed
        parameters['purpose'] = "Removed Numbers"
        parameters['analyzed'] = analyzed
        flag = 1

    if request.POST.get('removeNewLine','off') == "on":
        received_text = text
        analyzed = ""
        for char in received_text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        text = analyzed
        parameters['purpose'] = "Removed New Lines"
        parameters['analyzed'] = analyzed
        flag = 1

    if request.POST.get('charcount','off') == "on":
        received_text = text
        analyzed = 0
        for char in received_text:
            if char != ' ':
                analyzed += 1
        text = analyzed
        parameters['purpose'] = "Character count (white spaces not included)"
        parameters['analyzed'] = analyzed
        flag = 1

    if flag == 0:
        return HttpResponse('<h2>Please select any option</h2>')

    return render(request, 'analyzed.html', parameters)

