from django.shortcuts import render, get_object_or_404
from  django.http import HttpResponse
from . models import Featured as FeaturedModel , Latest as LatestModel ,Deals , Trending as TrendingModel
# from .filter import UserFilter
# from django.views.generic import DetailView
# Create your views here.


def Homeview(request, *args, **kwargs):
    Trending1 = TrendingModel.objects.order_by("-id")
    Featured2 = FeaturedModel.objects.order_by("-id")
    Latest3 = LatestModel.objects.order_by("-id")
    Deals4  = Deals.objects.order_by("-id")
    context = {
        'Trending' : Trending1,
        'Featured' :  Featured2,
        'Latest' : Latest3,
        'Deals' : Deals4  

    }
    return render(request, "index.html",context)
# the header   
def Latest(request):
    Latest3 = LatestModel.objects.order_by("-id")
    context = {
        'Latest' : Latest3,
    }
    return render(request, "latest.html",context)

def Trending(request, *args, **kwargs):
    Trending3 = TrendingModel.objects.order_by("-id")
    context = {
        'Trending' :  Trending3,
    }
    return render(request, "trend.html",context)
def Featured(request):
    Featured3 = FeaturedModel.objects.order_by("-id")
    context = {
        'Featured' : Featured3,
    }
    return render(request, "featured.html",context)






# section



def DetailViewTrending(request, slug):
    post = get_object_or_404(TrendingModel, slug=slug )
    
    return render(request, "direct.html",{'Trending': post} )


def DetailViewLatest(request, slug):
    post = get_object_or_404(LatestModel, slug=slug)
    
    return render(request, "directlatest.html",{'Latest': post} )


def DetailViewFeatured(request, slug):
    post = get_object_or_404(FeaturedModel, slug=slug)
    
    return render(request, "directfeature.html",{'Featured': post} )

# def searchbar(request):
#     if request.method == 'GET':
#         search = request.GET.get('search')
#         Trending1 =Trending.objects.all().filter(category=search)
#         return render(request, 'search.html', {'trend': Trending1})
    
# def DetailViewDeals(request, pk):
#     post = get_object_or_404(Deals, pk=pk)
    
#     return render(request, "directdeals.html",{'Deal': post} )
    
