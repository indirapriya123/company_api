from django.http import HttpResponse
def home_page(request):
    print("This is Home Page")

    return HttpResponse("This is Home Page")            