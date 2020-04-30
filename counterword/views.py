from django.http import HttpResponse #Djangho code to return http response to users
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html') #WHEN CALLED IT GOES TO home.html to print out something to users

def aboutpage(request):
    return render(request, 'about.html') #WHEN CALLED IT GOES TO home.html to print out something to users


def count(request): #tells us alot about a request coming into a website
    fulltext = request.GET['fulltext'] #gets the full text from  the website URL so after the "?"
    #print(fulltext)
    wordlist = fulltext.split() #splits text to different words

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1
        else:
            #add to the worddictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse= True)
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist),'sortedwords':sortedwords})
