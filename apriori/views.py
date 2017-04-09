from django.shortcuts import render

from django.http import HttpResponse
from apriori.apyori import apriori
from apriori.ap import runApriori, dataFromFile
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

def index2(request):
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

def index(request):
    minSupport = 0.2
    minConfidence = 0.5
    inFile = dataFromFile('apriori/dataset.csv')
    print("got file")
    html = ""
    items, rules = runApriori(inFile, minSupport, minConfidence)
    print("return from apriori")
    for item, support in items:
        #sorted(items, key=lambda support: support):
        html += "item: %s , %.3f" % (str(item), support)
        print(html)

    html += '\n------------------------ RULES:'

    for rule, confidence in rules:
        #sorted(rules, key=lambda confidence: confidence):
        pre, post = rule
        html += "Rule: %s ==> %s , %.3f" % (str(pre), str(post), confidence)
        print(html)
    return HttpResponse(html)