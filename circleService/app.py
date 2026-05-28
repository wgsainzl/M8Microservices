from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route('/area', methods=['GET'])
def area():
    radio = float(request.args.get('radio', 0))
    resultado = math.pi * (radio ** 2)
    return jsonify({'figura': 'círculo', 'área': resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
