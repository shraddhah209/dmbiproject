from django.shortcuts import render

from django.http import HttpResponse
from apriori.apyori import apriori
from django.template import loader
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
    minSupport = 0.0
    minConfidence = 0.0
    inFile = dataFromFile('apriori/dataset.csv')
    print("got file")
    html = ""
    items, rules = runApriori(inFile, minSupport, minConfidence)
    print("return from apriori")

    '''logic'''


    context = {

    }
    a = "New York"
    b = "MBE"
    itemSet = set()
    itemSet.add(a)
    itemSet.add(b)

    for item, support in items:
        list(item)
        set(item)
        '''for i in item:
            html += str(i) + "<br>" '''
        #sorted(items, key=lambda support: support):
        #html += str(itemSet)
        #html += str(item)
        if itemSet.issubset(item):
            html += "item:"+str(item)+" %.3f<br>" % (support)
            for i in item:

                print(html)

    html += '------------------------ RULES:'

    '''for rule, confidence in rules:
        #sorted(rules, key=lambda confidence: confidence):
        pre, post = rule
        html += "Rule: %s ==> %s , %.3f" % (str(pre), str(post), confidence)
        print(html)
    #template = loader.get_template("apriori/output.html") '''
    return HttpResponse(html) #template.render(context, request))