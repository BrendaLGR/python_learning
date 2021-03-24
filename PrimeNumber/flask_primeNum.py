from flask import Flask, jsonify, request
from primeNumber import is_prime

app = Flask(__name__)

@app.route('/prime/<int:num>', methods=['GET'])
def get_primeNum(num):
    result = is_prime(num)
    if result == True:
        return jsonify({'numero': num, 'resultado': 'es primo'})
    else:
        return jsonify ({'numero': num, 'resultado': 'no es primo'})
if __name__ == '__main__':
    app.run(debug=True)