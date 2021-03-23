from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/exp/<int:num>/<int:ex>', methods=['GET'])
def get_exp(num,ex):
    return jsonify({'Square': num**ex})

if __name__ == '__main__':
    app.run(debug=True)
