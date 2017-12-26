from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils import timezone
from django.utils.timezone import utc
import datetime
from .models import Advert

# Create your views here.
def advert_list(request):
    adverts = Advert.objects.filter(created_date__lte=timezone.now()).order_by('category')
    return render(request, 'dsignage/advert_list.html', {'adverts': adverts})

def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('dsignage/advert_list.html',
                             context_instance=context)
LOGIN_REDIRECT_URL = '/'