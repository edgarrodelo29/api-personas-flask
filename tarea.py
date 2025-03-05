from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/personas', methods=['GET'])
def obtener_personas():
    lista_personas = ["Juan", "María", "Pedro", "Luisa", "Carlos"]
    return jsonify(lista_personas)

if __name__ == '__main__':
    app.run(debug=True)