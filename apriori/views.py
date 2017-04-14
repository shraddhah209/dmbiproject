from django.shortcuts import render

from django.http import HttpResponse
from apriori.apyori import apriori
from django.template import loader
from apriori.ap import runApriori, dataFromFile, getItemSetTransactionList
# Create your views here.
import pandas as pd
import numpy

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


def itemInput(request):
    inFile = dataFromFile('apriori/market.csv')
    input, T = getItemSetTransactionList(inFile)
    itemSet = []
    itemsort = []
    for x in input:
        itemSet.append(list(x))
    for i in itemSet:
        for x in i:
            itemsort.append(x)
    itemsort.sort()
    #print(itemsort)
    length = len(itemsort)

    print(length)
    context = {
        "itemSet": itemsort
    }
    #template = loader.get_template("apriori/output.html")
    #return HttpResponse(template.render(context, request))
    return render(request, 'apriori/output.html', context)

def index(request):
    input = request.POST.getlist('ch[]')
    set(input)
    '''
    a = "New York"
    b = "MBE"
    itemSet = set()
    itemSet.add(a)
    itemSet.add(b)'''

    minSupport = 0.006
    minConfidence = 0.02
    inFile = dataFromFile('apriori/market.csv')
    html = ""
    items, rules = runApriori(inFile, minSupport, minConfidence)
    itemSet = set()
    for x in input:
        itemSet.add(x)
    '''logic'''
    final = set()
    temp = set()
    for item, support in items:
        list(item)
        set(item)
        print(item)
        #sorted(items, key=lambda support: support):
        #html += str(itemSet)
        #html += str(item)
        # print(support)
        if itemSet.issubset(item):
            for i in item:
                temp.add(i)
                if not temp.issubset(itemSet):
                    final.add(i)
                    print(i)
                temp.remove(i)
    html += "<style>" \
            "</style><center><h2>Recommendations: </h2></center><br><br><h4>"
    for i in final:
        print(i)
        html += "<center>"+ str(i) +"<br>"
    html +="</h4>"
    html += "Confidence:<br>"
    for rule, confidence in rules:
        pre, post = rule
        html += "%s ----->  %s , %.3f<br>" % (str(pre), str(post), 100*confidence)
    return HttpResponse(html) #template.render(context, request))