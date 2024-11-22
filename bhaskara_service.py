from flask import Flask, request, jsonify
from flask_cors import CORS  

app = Flask(__name__)
CORS(app) 

@app.route('/bhaskara', methods=['POST', 'GET'])
def calcular_bhaskara():
    if request.method == 'POST':
        try:
            data = request.get_json()
            a = data.get('a')
            b = data.get('b')
            c = data.get('c')

            if a is None or b is None or c is None:
                return jsonify({"error": "Os coeficientes 'a', 'b' e 'c' são obrigatórios."}), 400
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
                return jsonify({"error": "Os coeficientes devem ser números."}), 400
            if a == 0:
                return jsonify({"error": "'a' não pode ser zero."}), 400

            delta = b**2 - 4*a*c

            if delta > 0:
                raiz1 = (-b + delta**0.5) / (2*a)
                raiz2 = (-b - delta**0.5) / (2*a)
                return jsonify({
                    "raizes": [raiz1, raiz2],
                    "tipo": "reais"
                })
            elif delta == 0:
                raiz = -b / (2*a)
                return jsonify({
                    "raizes": [raiz],
                    "tipo": "real"
                })
            else:
                real = -b / (2*a)
                imaginaria = (-delta)**0.5 / (2*a)
                return jsonify({
                    "raizes": [f"{real}+{imaginaria}i", f"{real}-{imaginaria}i"],
                    "tipo": "complexas"
                })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    elif request.method == 'GET':
        return jsonify({
            "message": "Use o método POST para enviar os coeficientes a, b, c para o cálculo de Bhaskara."
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
