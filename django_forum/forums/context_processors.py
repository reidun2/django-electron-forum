from .models import Category, Ad
import random

def all_categories(request):
    return {'all_categories': Category.objects.all()}

def random_ad(request):
    ads = Ad.objects.all()
    ad = random.choice(ads) if ads else None
    return {'ad': ad}