from PythonBack import Searching
from flask import Flask, render_template,request
import requests
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


app = Flask(__name__)


start = time.perf_counter()
searchClass = Searching.SearchClass()
#headers for requests the url 
@app.route('/')
def render_html():
    return render_template('./index.html',length = 0)
#on submit the form router
@app.route('/submit_form', methods=['POST', 'GET'])
def getFormValues():
    if request.method == 'POST':
        data = request.form.to_dict()
        search = data['search-text']
        startSearch = time.perf_counter()
        searchClass.searchFun(search)
        endSearch = time.perf_counter()
        print(endSearch - startSearch)


        # try:
        #     with ProcessPoolExecutor(max_workers = 20) as executor:
        #         futures = [executor.submit(searchClass.scrabEachWebsite, url) for url in searchClass.selectedLink]
               
        # except Exception as e: print(e)


        try:
            with ThreadPoolExecutor() as executor:
                resutls = executor.map( searchClass.scrabEachWebsite,searchClass.selectedLink,searchClass.selectedTitle)
            finished = time.perf_counter()
            print(finished - start)
        except Exception as e: print(e)


        return render_template('./index.html',submitform ="true",html=searchClass.searchResultDataLists,length=len(searchClass.searchResultDataLists))
    else:
        return "submiting from error"


if __name__ == '__main__': 
    app.debug = True
    app.run()
    app.run(debug = True)