from django.shortcuts import render
import stocks.scripts.searchStock as searchStock



# Create your views here.


def index(request):
    if request.method == 'POST':
        #POST request for stock information given ticker symbol
        identifier = request.POST.get('tckr').upper()
    else:
        #Default identifier used for API request
        identifier = ''

    context = {
        #Function call to find stock
        'searchStock': searchStock.curr_share_price(identifier)
    }

    #render the template index.html with params context(dictionary)
    return render(request, 'stocks/index.html', context)
