from django.shortcuts import redirect, render, render_to_response
from django.template import RequestContext


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'tracker/home.html')


def about(request):
    return render(request, 'tracker/about.html')


def handler404(request):
    response = render_to_response('main/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
