from flask import Flask, jsonify, request
from evenOdd import EvenOdd

app = Flask(__name__)

@app.route('/evenOdd/<int:num>', methods=['GET'])
def get_evenOdd(num):
    result = EvenOdd(num)
    if result == True:
        return jsonify({'numero ': num, 'resultado' : 'par'})
    else:
        return jsonify({'numero ': num, 'resultado' : 'impar'})

if __name__ == '__main__':
    app.run(debug=True)