from flask import Flask
from flask import request
from  predict import predict

app = Flask(__name__)
@app.route("/dm", methods=['GET'])
def index():
    return str(predict( request.args['keyword'] ))

if __name__ == "__main__":
    app.debug = True
    app.run(host='10.0.2.15', port=1234)
