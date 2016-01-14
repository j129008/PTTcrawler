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
            return render_template('app.html', foo='分析結果：這是基本五樓文')
        if result == 2:
            return render_template('app.html', foo='分析結果：這是中等五樓文')
        if result == 3:
            return render_template('app.html', foo='分析結果：這是高等五樓文')
        else:
            return render_template('app.html', foo='分析結果：這不會出現五樓')
    return render_template('app.html', foo='')


if __name__ == "__main__":
    app.debug = True
    app.run(host='10.0.2.15', port=1234)
