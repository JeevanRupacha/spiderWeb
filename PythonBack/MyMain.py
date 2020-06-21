import requests
import time
import threading
from bs4 import BeautifulSoup
from flask import Flask, request, render_template, Markup
# from multiprocessing import Pool
class MyMain:
    def __init__(self):
        # self.app = Flask(__name__, static_url_path='/static')
        self.selectedLink = []
        self.selectedTitle = []
        self.searchResultDataLists = []
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) self.leWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}



    def loopTheLink(self, i, links):
            h3 = links[i].find('h3')
            if h3 != None:
            #self.end the link href to selectedLink list
            #text.split("&",1)[0] replace all the string after the '&' character
                aLink = links[i].get('href').replace('/url?q=',"").split('&',1)[0]
                self.selectedLink.append(aLink.split('%',1)[0])
                self.selectedTitle.append(h3.get_text())
      
    #searching algorithm       
    def searchFun(self,search):
        self.selectedLink.clear()   
        self.selectedTitle.clear()
        self.searchResultDataLists.clear()   
        response = requests.get("https://www.google.com/search?q=" + search,headers = self.headers)
        soup = BeautifulSoup(response.text, 'lxml')
        #google result kCrYT class contains the links tags 
        #selecting <a> tag inside all the kCrYT class
        links = soup.select('.kCrYT a')
        #looping all the anker tag for links and head extract
        for i in range(len(links)):
            self.loopTheLink(i,links)






        #     t = threading.Thread(target=self.loopTheLink, args=[i, anker])
        #     t.start()
        #     threads.append(t)

        # for thread in threads:
        #     thread.join()
        

    

    #calcuation for each linked website function 
    def scrabEachWebsite(self, url):       
        if "youtube.com" not in url:
            responseweb = requests.get(url,headers=self.headers)
            soupweb = BeautifulSoup(responseweb.text, 'lxml')
            print(soupweb)
            self.webDataExtract(soupweb)
           
        


    #Extract the web data
    #this is algorithm for filtering the web data
    def webDataExtract(self,soup):
        #check article tag
        if (soup.find('article')):
            child = soup.find('article').find_all('div')
            return self.articleExtractor(child)

        #content id tag
        if (soup.find(id={'content'})):
            child = soup.find(id={'content'}).find_all('div')
            return self.articleExtractor(child)

        #content class tag
        if (soup.find(class_={'content'})):
            child = soup.find(class_={'content'}).find_all('div')
            return self.articleExtractor(child)

        #content-main id tag
        if (soup.find(id={'content-main'})):
            child = soup.find(id={'content-main'}).find_all('div')
            return self.articleExtractor(child)

        #content-main class tag
        if (soup.find(class_={'content-main'})):
            child = soup.find(class_={'content-main'}).find_all('div')
            return self.articleExtractor(child)
        
        #content-main id tag
        if (soup.find(id={'main_content'})):
            child = soup.find(id={'main_content'}).find_all('div')
            return self.articleExtractor(child)

        #content-main class tag
        if (soup.find(class_={'article-container'})):
            child = soup.find(class_={'content-main'}).find_all('div')
            return self.articleExtractor(child)



    # article extracting function *only by article tag
    #Extracts the all children od article tag i.e div tag and take largest length div
    def articleExtractor(self,child):
        big = ""
        for div in child:
            if(len(big)< len(div)):
                big = div
        self.searchResultDataLists.append(Markup(big))



    def display(self):
        for i in range(len(self.selectedTitle)):
            print(self.selectedLink[i])
            print(self.selectedTitle[i] + "\n\n")
    

