from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, User
from first_app.forms import  FormName, NewUserForm, FormAccessRecord
# Create your views here.


def hello(request, name=""):
    return HttpResponse("<em>Hello " + name + " </em>")

def strong(request):
    return HttpResponse("<strong>I'm strong</strong>")

def index(request):
    return render(request,'index.html')

def dashboard(request):
    return HttpResponse("<h2>THIS IS DASHBOARD</h2>")

def template_text_render(request):
    my_dict = {'insert_me': "HEY! This is coming from views.py"}
    return render(request, 'first_app/index.html', context=my_dict)


def template_image_injection(request):
    return render(request, 'first_app/image.html')


def table(request):
    webpage = AccessRecord.objects.order_by('date')
    my_dict = {'access_record': webpage}
    return render(request, 'table.html', context=my_dict)


def form_name_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])
    return render(request,'form_page.html',{'form':form})
        # else:
        #     return render(request,'index.html')


def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'users.html',{'form':form})


def accessRecord(request):

    form = FormAccessRecord()

    if request.method == "POST":
        form = FormAccessRecord(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'users.html',{'form':form})


def base(request):
    my_dict = {'text': "hello world", 'number': '100'}
    return render(request,'base.html', context=my_dict)

def other(request):
    return render(request,'other.html')

def relative(request):
    return render(request,'relative_url_templates.html')
