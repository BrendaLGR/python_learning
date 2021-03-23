from flask import Flask, jsonify, request
from factorialNum import factorial

app = Flask(__name__)

@app.route('/factorial/<int:num>', methods=['GET'])
def get_factorial(num):
    return jsonify({'Factorial': factorial(num)})
if __name__ == '__main__':
    app.run(debug=True)