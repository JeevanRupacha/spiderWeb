from PythonBack import MyMain
from flask import Flask, render_template,request
import requests
import time
import threading
import concurrent.futures
import multiprocessing

app = Flask(__name__)

start = time.perf_counter()

m = MyMain.MyMain()
#headers for requests the url 
@app.route('/')
def render_html():
    return render_template('./index.html',html=m.searchResultDataLists,length=len(m.selectedLink),selectedLink=m.selectedLink,selectedTitle=m.selectedTitle)


#on submit the form router
@app.route('/submit_form', methods=['POST', 'GET'])
def getFormValues():
    if request.method == 'POST':
        data = request.form.to_dict()
        search = data['search-text']
        m.searchFun(search)

        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map( m.scrabEachWebsite,m.selectedLink)

        except:
            print("error")
        # process = []
        # for i in range(len(m.selectedLink)):
        #     p = multiprocessing.Process(target=m.scrabEachWebsite, args=[m.selectedLink[i]])
        #     p.start()
        #     process.append(p)

        # for pro in process:
        #     pro.join()
         
        finished = time.perf_counter()
        print( finished - start )
        return render_template('./index.html',submitform ="true",html=m.searchResultDataLists,length=len(m.selectedLink),selectedLink=m.selectedLink,selectedTitle=m.selectedTitle)
    else:
        return "submiting from error"



if __name__ == '__main__': 
    app.debug = True
    app.run()
    app.run(debug = True)