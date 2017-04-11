from django.shortcuts import render

from django.http import HttpResponse
from apriori.apyori import apriori
from django.template import loader
from apriori.ap import runApriori, dataFromFile, getItemSetTransactionList
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


def itemInput(request):
    inFile = dataFromFile('apriori/market.csv')
    input, T = getItemSetTransactionList(inFile)
    itemSet = []
    for x in input:
        itemSet.append(list(x))

    context = {
        "itemSet": itemSet
    }
    #template = loader.get_template("apriori/output.html")
    #return HttpResponse(template.render(context, request))
    return render(request, 'apriori/output.html', context)

def index(request):

    input = set()
    input = request.POST.getlist('ch[]')
    set(input)
    '''
    a = "New York"
    b = "MBE"
    itemSet = set()
    itemSet.add(a)
    itemSet.add(b)'''

    minSupport = 0.0
    minConfidence = 0.0
    inFile = dataFromFile('apriori/market.csv')
    print("got file")
    html = ""
    items, rules = runApriori(inFile, minSupport, minConfidence)

    itemSet1 = []
    print("return from apriori")
    html += str(input)
    '''logic'''

    for item,support in items:
        set(item)
        print(item)

    '''
     for item, support in items:
        list(item)
        set(item)
        #sorted(items, key=lambda support: support):
        #html += str(itemSet)
        #html += str(item)
        print(support)
        if itemSet.issubset(item):
            #html += "item:"+str(item)+" %.3f<br>" % (support)
            for i in item:
                temp.add(i)
                if not temp.issubset(itemSet):
                    final.add(i)
                temp.remove(i)
                #print(html)
    html += str(final)
    html += '------------------------ RULES:'

    for rule, confidence in rules:
        #sorted(rules, key=lambda confidence: confidence):
        pre, post = rule
        html += "Rule: %s ==> %s , %.3f" % (str(pre), str(post), confidence)
        print(html)    '''
    #template = loader.get_template("apriori/output.html")
    return HttpResponse(html) #template.render(context, request))