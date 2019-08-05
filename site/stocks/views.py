from django.shortcuts import render
import stocks.scripts.searchStock as searchStock



# Create your views here.


def index(request):
    if request.method == 'POST':
        identifier = request.POST.get('tckr').upper()
    else:
        identifier = ''

    context = {
        'searchStock': searchStock.curr_share_price(identifier)
    }

    return render(request, 'stocks/index.html', context)
