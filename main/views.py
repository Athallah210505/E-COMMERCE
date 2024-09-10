from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'gold_name' : 'Gold 24K',
        'description': '24K Gold is pure gold. Even though it is called pure gold, 100% purity is unattainable, therefore “pure gold” refers to gold that is between 99.7% and 99.9% gold. Also known as fine gold, pure gold hasn’t been made stronger with other metals, therefore it maintains its rich yellow hue and is a lot softer than other types of gold. Because of this (and because it is so expensive), 24 karat gold jewelry is very rare in the United States. It is, however, a lot more popular in China, India and other Asian countries—especially for investment purposes. ',
        'quantity': '1',
        'price' : 'Rp.10.000.000',
        'name' : 'Athallah Nadhif',
        'npm' : '2306275651',
        'kelas' : 'PBP B',
    }

    return render(request, "main.html", context)