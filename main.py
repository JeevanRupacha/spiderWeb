import requests
from bs4 import BeautifulSoup
from flask import Flask, request,render_template,Markup

app = Flask(__name__, static_url_path='/static')
selectedLink = []
selectedTitle = []
searchResultDataLists = []



@app.route('/')
def render_html():
    return render_template('./index.html',html=searchResultDataLists,length=len(selectedLink),selectedLink=selectedLink,selectedTitle=selectedTitle)


#on submit the form router
@app.route('/submit_form', methods=['POST', 'GET'])
def getFormValues():
    if request.method == 'POST':
        data = request.form.to_dict()
        search = data['search-text']
        searchFun(search)
        for i in range(len(selectedLink)):
            scrabEachWebsite(selectedLink[i],selectedTitle[i])

        return render_template('./index.html',submitform ="true",html=searchResultDataLists,length=len(selectedLink),selectedLink=selectedLink,selectedTitle=selectedTitle)
    else:
        return "submiting from error"



#searching algorithm       
def searchFun(search):
    selectedLink.clear()   
    selectedTitle.clear()
    searchResultDataLists.clear()   
    response = requests.get("https://www.google.com/search?q=" + search)
    print(response.url)
    soup = BeautifulSoup(response.text, 'lxml')
    #google result kCrYT class contains the links tags 
    #selecting <a> tag inside all the kCrYT class
    anker = soup.select('.kCrYT a')
    #looping all the anker tag for links and head extract
    for i in range(len(anker)):
        h3 = anker[i].find('h3')
        if h3 != None:
            #append the link href to selectedLink list
            print(anker[i])
            #text.split("&",1)[0] replace all the string after the '&' character
            aLink = anker[i].get('href').replace('/url?q=',"").split('&',1)[0]
            selectedLink.append(aLink.split('%',1)[0])
            selectedTitle.append(h3.get_text())
    display()    

#calcuation for each linked website function 
def scrabEachWebsite(url,title):
    if "youtube.com" not in url:
        responseweb = requests.get(url)
        soupweb = BeautifulSoup(responseweb.text, 'lxml')
        webDataExtract(soupweb)


#Extract the web data
#this is algorithm for filtering the web data
def webDataExtract(soup):
    #check article tag
    if (soup.find('article')):
        child = soup.find('article').find_all('div')
        return articleExtractor(child)

    #content id tag
    if (soup.find(id={'content'})):
        child = soup.find(id={'content'}).find_all('div')
        return articleExtractor(child)

    #content class tag
    if (soup.find(class_={'content'})):
        child = soup.find(class_={'content'}).find_all('div')
        return articleExtractor(child)

    #content-main id tag
    if (soup.find(id={'content-main'})):
        child = soup.find(id={'content-main'}).find_all('div')
        return articleExtractor(child)

    #content-main class tag
    if (soup.find(class_={'content-main'})):
        child = soup.find(class_={'content-main'}).find_all('div')
        return articleExtractor(child)

    #content-main class tag
    if (soup.find(class_={'article-container'})):
        child = soup.find(class_={'content-main'}).find_all('div')
        return articleExtractor(child)



# article extracting function *only by article tag
#Extracts the all children od article tag i.e div tag and take largest length div
def articleExtractor(child):
    big = ""
    for div in child:
        if(len(big)< len(div)):
            big = div
    searchResultDataLists.append(Markup(big))



def display():
    for i in range(len(selectedTitle)):
        print(selectedLink[i])
        print(selectedTitle[i] + "\n\n")
 


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)