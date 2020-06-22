from PythonBack import MyMain
from flask import Flask, render_template,request
import requests
import time
import threading
from concurrent.futures import ProcessPoolExecutor, as_completed
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

        # try:
        #     with ProcessPoolExecutor(max_workers=4) as executor:
        #         start = time.time()
        #         futures = [executor.submit(m.scrabEachWebsite, url) for url in m.selectedLink]
        #         results = []
        #         for result in as_completed(futures):
        #             results.append(result)
        #         end = time.time()
        #         print("Time Taken: {:.6f}s".format(end - start))
        # except:
        #     print(EOFError)



        # try:
        #     with concurrent.futures.ThreadPoolExecutor() as executor:
        #         executor.map( m.scrabEachWebsite,m.selectedLink)

        # except:
        #     raise(Exception)
        # process = []
        # try:
        #     for i in range(len(m.selectedLink)):
        #         p = multiprocessing.Process(target=m.scrabEachWebsite, args=[m.selectedLink[i]])
        #         p.start()
        #         process.append(p)

        #     for pro in process:
        #         pro.join()
        # except:
        #     print("error herer")
        for i in range(len(m.selectedLink)):
            m.scrabEachWebsite(m.selectedLink[i])
         
        finished = time.perf_counter()
        print( finished - start )
        return render_template('./index.html',submitform ="true",html=m.searchResultDataLists,length=len(m.selectedLink),selectedLink=m.selectedLink,selectedTitle=m.selectedTitle)
    else:
        return "submiting from error"



if __name__ == '__main__': 
    app.debug = True
    app.run()
    app.run(debug = True)