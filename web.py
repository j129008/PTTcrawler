from flask import Flask
from flask import request
from  predict import predict
from flask import render_template

app = Flask(__name__)

@app.route("/")
def indexGet():
    if 'keyword' in request.args:
        result = predict( request.args['keyword'] )
        if result == 1:
            return render_template('app.html', foo='成功！')
    return render_template('app.html', foo='失敗')


if __name__ == "__main__":
    app.debug = True
    app.run(host='10.0.2.15', port=1234)
