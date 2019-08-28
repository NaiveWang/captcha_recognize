from flask import Flask, render_template, make_response, request
from urllib import request as req
import random
import os
import glob
app = Flask(__name__)
img = 'temp.png'
url = 'https://login.sina.com.cn/cgi/pin.php'

@app.route('/', methods=['GET'])
def hub():
    req.urlretrieve(url, img)
    return render_template('root.html', result = 'Hub refreshed.')

@app.route('/', methods=['POST'])
def hub_act():
    if 'g' in request.form:
        req.urlretrieve(url, img)
        return render_template('root.html', result = 'image downloaded.')
    elif 'c'in request.form:
        return render_template('root.html', result = 'cracking branch, not implemented yet.')
    elif 's' in request.form:
        label = request.form['_']
        #file operation
        os.popen('cp %s ../lib/%s_%s.jpg'%(img, label, random.randint(100000,999999).__str__()))
        req.urlretrieve(url, img)
        return render_template('root.html', result = len(glob.glob('../lib/*.jpg')).__str__()+', save file to lib #'+label)
    return render_template('root.html', result = 'default branch.')

@app.route('/temp.png', methods=['GET'])
def image():
    try:
        resp = make_response(open(img, 'rb').read())
        resp.content_type = "image/jpeg"
        return resp
    except Exception as e:
        return None
@app.route('/gen.php')
def gen():
    return render_template('pin.php')

if __name__ == "__main__":
    app.run(debug=False)
