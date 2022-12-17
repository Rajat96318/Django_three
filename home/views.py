from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # dictionary = {'name':'rajat', 'address':'manduadih'}
    return render(request, 'index.html')
    # return HttpResponse('''<h1>RAJAT is noob</h1> <a href="https://www.w3schools.com">Visit W3Schools.com!</a>
# ''')


def analyze(request):
    djtext = request.POST.get('text', 'default')

    # Check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    removeextraspace = request.POST.get('removeextraspace', 'off')
    countcharacter = request.POST.get('countcharacter', 'off')

    # print(removepunc)
    # print(djtext)
    # analyzed = djtext

    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""

    if removepunc == "on":
        for char in djtext:
            if char not in punctuation:
                analyzed += char
        params={'purpose':'Removed punctions', 'analyzed_text':analyzed}
        djtext=analyzed
    
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params={'purpose':'Uppercasee', 'analyzed_text':analyzed}
        djtext=analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char!='\r':
                analyzed += char
        params={'purpose':'Uppercasee', 'analyzed_text':analyzed}
        djtext=analyzed

    if removeextraspace == "on":
        analyzed = ""
        for i, char in enumerate(djtext):
            if not(djtext[i]==' ' and djtext[i+1]==' '):
                analyzed += char
        params={'purpose':'Removing extra space', 'analyzed_text':analyzed}
        djtext=analyzed

    if countcharacter == "on":
        c=0
        for char in djtext:
            if char >= 'a' and char <= 'z':
                c = c + 1
        params={'purpose':'Removing extra space', 'analyzed_text':c}

    if(countcharacter != "on" and removeextraspace != "on" and newlineremover != "on" and fullcaps != "on" and 
    removepunc != "on"):
        return HttpResponse("Eroor")
    # else:
    #     return HttpResponse("Error")
    
    return render(request, 'analyze.html', params)




# def read_file(request):
#     f = open('C:/Users/INDIA/Desktop/codeWithHarry_Django/django_me_1/home/one.txt', 'r')
#     file_content = f.read()
#     f.close()
#     return HttpResponse(file_content)

# def aage(request):
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     return HttpResponse('''<h3>aage jane k liye click kare</h3><a href="/piche"><button>AAGE</button></a>''')

# def piche(request):
#     return HttpResponse('''<h3>piche jane k liye click kare</h3><a href="/aage"><button>PICHE</button></a>''')
