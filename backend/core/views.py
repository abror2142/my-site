from django.shortcuts import render
from .models import Promotion
from django.utils import timezone
# Create your views here.

def home_view(request):
    now = timezone.now()
    promotions = Promotion.objects.filter(start_date__lte=now, end_date__gte=now)
    state = {
        "promotions": promotions,
    }
    return render(request, "index.html", state)