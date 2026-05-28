from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

#Esto debe cuadrar con los puertos de yaml
TRIANGLE_URL = "http://triangle:5100/area"
SQUARE_URL = "http://square:5101/area"
CIRCLE_URL = "http://circle:5102/area"


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "mensaje": "API Gateway de microservicios",
        "endpoints": {
            "triangulo": "/area/triangulo?base=10&altura=5",
            "cuadrado": "/area/cuadrado?lado=4",
            "circulo": "/area/circulo?radio=3"
        }
    })

@app.route('/area/triangulo', methods=['GET'])
def area_triangulo():
    try:
        base = request.args.get('base')
        altura = request.args.get('altura')

        respuesta = requests.get(TRIANGLE_URL, params={
            "base": base,
            "altura": altura
        })

        return jsonify(respuesta.json()), respuesta.status_code
    except Exception as e:
        return jsonify({'error': f'Error al conectar con triangleService-service: {str(e)}'}), 500

@app.route('/area/cuadrado', methods=['GET'])
def area_cuadrado():
    try:
        lado = request.args.get('lado')

        respuesta = requests.get(SQUARE_URL, params={
            "lado": lado
        })

        return jsonify(respuesta.json()), respuesta.status_code
    except Exception as e:
        return jsonify({'error': f'Error al conectar con squareService-service: {str(e)}'}), 500

@app.route('/area/circulo', methods=['GET'])
def area_circulo():
    try:
        radio = request.args.get('radio')

        respuesta = requests.get(CIRCLE_URL, params={
            "radio": radio
        })

        return jsonify(respuesta.json()), respuesta.status_code
    except Exception as e:
        return jsonify({'error': f'Error al conectar con circleService-service: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
