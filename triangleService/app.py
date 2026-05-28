from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/area', methods=['GET'])
def area():
    base = float(request.args.get('base', 19))
    altura = float(request.args.get('altura', 5))
    resultado = (base * altura) / 2
    return jsonify({'figura': 'triángulo', 'área': resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
