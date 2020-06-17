import requests
from bs4 import BeautifulSoup
from flask import Flask, request,render_template,Markup

app = Flask(__name__)
selectedLink = []
selectedTitle = []
linkHtml = []
html = Markup("<h1>This is test </h1>")

@app.route('/')
def render_html():
    return render_template('./index.html',html=html)

@app.route('/submit_form', methods=['POST', 'GET'])
def getFormValues():
    if request.method == 'POST':
        data = request.form.to_dict()
        search = data['search-text']
        searchFun(search)
        return render_template('./result.html',html=html,length=len(selectedLink),selectedLink=selectedLink,selectedTitle=selectedTitle)
    else:
        return "submiting from error"

 #searching algorithm       
def searchFun(search):     
    response = requests.get("https://www.google.com/search?q=" + search)
    print(response.url)
    soup = BeautifulSoup(response.text, 'lxml')
    #google result kCrYT class contains the links tags 
    links = soup.select('.kCrYT')
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
            selectedLink.append(aLink)
            selectedTitle.append(h3.get_text())
    display()    

print(len(selectedTitle))
print(len(selectedLink))


def display():
    for i in range(len(selectedTitle)):
        print(selectedLink[i])
        print(selectedTitle[i] + "\n\n")
 
if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)