from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.shortcuts import resolve_url
from .models import ShortUrl

def show_view(request,**kwargs):
    short_url = get_object_or_404(ShortUrl,**kwargs)
    lista_urls = ShortUrl.objects.all().order_by('-count');
    lista_url_curta = ShortUrl.objects.all().order_by('-code')[:5:0];
    lista_url_redirect = ShortUrl.objects.all().order_by('-count')[:5:1];
    print(request.META)
    return render(request,'shorted.html',locals())

def redirect_view(request,**kwargs):
    short_url = get_object_or_404(ShortUrl,**kwargs)
    short_url.count += 1
    short_url.save(update_fields=['count'])
    return redirect(short_url)

class ShortUrlCreateView(CreateView):
    model = ShortUrl
    fields = ['url']
    template_name = 'home.html'

    def get_success_url(self):
        return resolve_url('shortener:url-preview',code=self.object.code)

