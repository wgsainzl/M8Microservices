from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/area', methods=['GET'])
def area():
    lado = float(request.args.get('lado', 5))
    resultado = lado * lado
    return jsonify({'figura': 'cuadrado', 'área': resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
