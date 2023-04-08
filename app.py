from flask import Flask # impoerted flask library
from flask import request #It will able to request the data from client page

app = Flask(__name__) # we are trying to create object of flask we have imported with help of dunder varible
'''where we are trying to decorate flaskfunction as it is going to create server after reaching to flask
server(that nothing but system ) then we trying to reach the function hello world, so with help of root (\)we are trying to expose function outside '''

@app.route("/") 
def hello_world():    #we have function called as hello world trying to return strin hello world
    return "<h1>Hello, World!</h1>"

@app.route("/hello1") 
def hello_world1():    
    return "<h1>Hello, World!1</h1>"

@app.route("/hello2") 
def hello_world22():    
    return "<h1>Hello, World!2</h1>"

@app.route("/input_url") 
def request_input():
    data = request.args.get('X')
    return "This is a data taken from url {}".format(data)

''' to hit above function we have to copy the link with local code then call this function with route 
then put ? the call argument, here it is 'X' Then = pass the data. example "https://black-nurse-qbiql.pwskills.app:5000/input_url?X=ANAMIKA" ,
this function take client request from url, get() fuction take the data from url'''

if __name__=="__main__":
    app.run(host="0.0.0.0")


''' for calling this from browser step1- run this code in flask step2- copy the http link add ":5000/function name " (https://black-nurse-qbiql.pwskills.app:5000/hello1) for calling hello world1 function'''
