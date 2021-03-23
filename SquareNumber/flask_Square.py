from flask import Flask, jsonify, request
from NumSquare import squareNum

app = Flask(__name__)

@app.route('/exp/<int:num>/<int:ex>', methods=['GET'])
def get_exp(num,ex):
    return jsonify({'Square':squareNum(num,ex)})

if __name__ == '__main__':
    app.run(debug=True)
