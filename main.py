from python import MyMain
from flask import Flask, render_template,request
import requests
import time
import threading 

app = Flask(__name__)

m = MyMain.MyMain()
#headers for requests the url 
@app.route('/')
def render_html():
    return render_template('./index.html',html=m.searchResultDataLists,length=len(m.selectedLink),selectedLink=m.selectedLink,selectedTitle=m.selectedTitle)


#on submit the form router
@app.route('/submit_form', methods=['POST', 'GET'])
def getFormValues():
    start = time.perf_counter()
    if request.method == 'POST':
        data = request.form.to_dict()
        search = data['search-text']
        m.searchFun(search)
        threads = []
        for i in range(len(m.selectedLink)):
            t = threading.Thread(target=m.scrabEachWebsite, args=[m.selectedLink[i],m.selectedTitle[i]])
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()
       
        finished = time.perf_counter()


        print( finished - start )
        return render_template('./index.html',submitform ="true",html=m.searchResultDataLists,length=len(m.selectedLink),selectedLink=m.selectedLink,selectedTitle=m.selectedTitle)
    else:
        return "submiting from error"


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)