from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Dados simulados em memória (para não precisarmos de banco de dados agora)
sensores = [
    {"id": 1, "tipo": "Temperatura", "status": "Ativo"},
    {"id": 2, "tipo": "Umidade", "status": "Inativo"}
]

@app.route('/')
def home():
    return "API RESTful de Sensores - Ativa!"

# Rota GET para listar todos os sensores
@app.route('/api/sensores', methods=['GET'])
def get_sensores():
    return jsonify(sensores)

# Rota POST para adicionar um novo sensor
@app.route('/api/sensores', methods=['POST'])
def add_sensor():
    novo_sensor = request.get_json()
    
    # Validação simples
    if not novo_sensor or 'tipo' not in novo_sensor:
        return jsonify({"erro": "Dados inválidos. O campo 'tipo' é obrigatório."}), 400
        
    novo_sensor['id'] = len(sensores) + 1
    sensores.append(novo_sensor)
    return jsonify(novo_sensor), 201

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
