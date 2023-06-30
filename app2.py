from flask import Flask

app = Flask(__name__)

# PROVES
@app.route('/components/prova')
def prova():
    return 'tot be'


# PRODUCCIÓ
@app.route('/')
def login():
    return 'prova'


if __name__ == '__main__':
    app.run()