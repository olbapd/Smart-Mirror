import requests
import time


#Info suministrated by Newsapi.org




#Gets the information form the source list 
def getNews(contSource,sources):
    url = ('https://newsapi.org/v2/top-headlines?sources='+sources[contSource]+'&apiKey=ce579b2e7ae441d0830cce3bc04fd534')
    contArticle=0
    newsList=[]
    while (contArticle<3):
        nData = requests.get(url).json()
        nAuthor=nData['articles'][contArticle]['source']['name']
        nTitle=nData['articles'][contArticle]['title']
        contArticle+=1
        newsList.append(nTitle)
    else:
        return newsList


#Makes a search for news depending on the keyword
def searchNews(keyword):
    url='https://newsapi.org/v2/everything?q='+keyword+'&apiKey=ce579b2e7ae441d0830cce3bc04fd534'
    contArticle=0
    while (contArticle<3):
        nData = requests.get(url).json()
        nAuthor=nData['articles'][contArticle]['source']['name']
        nTitle=nData['articles'][contArticle]['title']
        nDescription=nData['articles'][contArticle]['description']
        print ("News from: "+nAuthor)
        print (nTitle)
        print (nDescription)
        print ("")

        contArticle+=1
    else:
        print("-------------------------------------------------------")
        time.sleep(5)





