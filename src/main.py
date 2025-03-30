from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello World!'

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO GET\n"
    elif request.method == 'POST':
        return "ECHO POST\n"
    elif request.method == 'PATCH':
        return "ECHO PATCH\n"
    elif request.method == 'PUT':
        return "ECHO PUT\n"
    elif request.method == 'DELETE':
        return "ECHO DELETE\n"
    

if __name__ == '__main__':
    app.run()