from django.shortcuts import render

from django.http import HttpResponse
from apriori.apyori import apriori

# Create your views here.
import pandas as pd

def index2(request):
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

def index(request):
    dataset = pd.read_csv('apriori/market.csv', header=None)
    transactions = []
    for i in range(0, 7501):
        print(i)
        transactions.append([str(dataset.values[i, j]) for j in range(0, 20)])

    rules = apriori(transactions, min_support=0.003, min_confidence=0.2, min_lift=3, min_length=2)

    results = list(rules)
    myResults = [list(x) for x in results]
    html = str(myResults)

    return HttpResponse(html)