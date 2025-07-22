from django.http import HttpResponse

def orders_home(request):
    return HttpResponse("<h1>هذه صفحة الطلبات مؤقتًا</h1>")
