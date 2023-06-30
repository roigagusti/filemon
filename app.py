from flask import Flask, render_template
from classes.functions import components,cases,projects,headers

app = Flask(__name__)


# FUNCTIONS
def componentsDict(cases_of_study, headers):
    output = {}
    for case in cases_of_study:
        output[case] = [header for header in headers if header.case == case]
    return output


# PROVES
@app.route('/components/prova')
def prova():
    a = ''   
    return a


#PRODUCCIÓ
@app.route('/')
def login():
    return 'tot be'

@app.route('/components/evolution')
def kpi():
    return render_template('evolution.html',components=components,cases=cases,projects=projects,headers=headers)

@app.route('/rompeflix/sync')
def rompeflix():
    a = ''
    return a

if __name__ == '__main__':
    app.run()
    #app.run(port=16400)