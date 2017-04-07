from django.shortcuts import render

from django.http import HttpResponse
from apriori.apyori import apriori
# Create your views here.


def index(request):
    html = "hi"
    transactions = [
        ['beer', 'nuts'],
        ['beer', 'cheese'],
        ['beer','nuts','milk'],
        ['beer','nuts','coco'],
    ]
    results = list(apriori(transactions))
    html += str(results)
    return HttpResponse(html)