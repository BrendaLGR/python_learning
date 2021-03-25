from flask import Flask, jsonify, request
from primeNumber import is_prime

app = Flask(__name__)

@app.route('/prime/<int:num>', methods=['GET'])
def get_primeNum(num):
    if is_prime(num):
        return jsonify({'numero': num, 'resultado': 'es primo'})
    else:
        return jsonify ({'numero': num, 'resultado': 'no es primo'})
if __name__ == '__main__':
    app.run(debug=True)