import requests
import time


#Info suministrated by Newsapi.org

#Automatic news True
news=True


#Gets the information form the source list 
def getNews():
    sources=["bbc-news","espn","cnn","fox-sports","marca","the-verge","crypto-coins-news","engadget","ign","abc-news","business-insider",
             "mtv-news","national-geographic","techradar"]
    contSource=0
    while(news):
        if (contSource<len(sources)):
            url = ('https://newsapi.org/v2/top-headlines?sources='+sources[contSource]+'&apiKey=ce579b2e7ae441d0830cce3bc04fd534')
            contSource+=1
            contArticle=0
            while (contArticle<3):
                nData = requests.get(url).json()
                nAuthor=nData['articles'][contArticle]['source']['name']
                nTitle=nData['articles'][contArticle]['title']
                nDescription=nData['articles'][contArticle]['description']
                if(contArticle==0):
                    print ("News from: "+nAuthor)
                print (nTitle)
                print (nDescription)
                print ("")
                contArticle+=1
            else:
                print("-------------------------------------------------------")
                time.sleep(5)
        else:
            contSource=0
            time.sleep(10)

getNews()

#Makes a search for news depending on the keyword
def searchNews():
    keyword=input("Search for: ")
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
        contArticle+=1
    else:
        print("-------------------------------------------------------")
        time.sleep(5)
