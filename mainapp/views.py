from django.http import HttpResponse

def main_view(request):
    return HttpResponse('It is main page without a template.')
