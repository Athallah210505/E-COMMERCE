from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'gold_name' : 'Pure Gold',
        'description': 'Pure Gold Bar with a weight of 1 kg',
        'quantity': '1',
        'price' : 'Rp.10.000.000'
    }

    return render(request, "main.html", context)