import requests


#Info suministrated by Newsapi.org
#ce579b2e7ae441d0830cce3bc04fd534
def getNews():
    sources=["bbc-news","espn","cnn","fox-sports","marca","the-verge"]
    
    url = ('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=ce579b2e7ae441d0830cce3bc04fd534')
    cont=0
    while (cont<3):
        nData = requests.get(url).json()
        nAuthor=nData['articles'][cont]['author']
        nTitle=nData['articles'][cont]['title']
        nDescription=nData['articles'][cont]['description']
        cont+=1
        print (nAuthor)
        print (nTitle)
        print (nDescription)
    else:
        print("There are no news left")
    

getNews()
