from flask import Flask, url_for, request, json, Response
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
    
@app.route('/messages', methods = ['POST'])
def api_message():
    
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data
    
    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)
    
    elif request.headers['Content-Type'] ==  'application/octet-stream':
        f = open('/binary', 'wb')
        f.write(request.data)
        f.close
        return 'Binary message written!'
    
    else:
        return "415 Unsupported Media Type! ;)"
    


if __name__ == '__main__':
    app.run()