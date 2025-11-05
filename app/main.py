from flask import Flask, jsonify, request
import joblib
import json
import os

# Cria o app Flask
app = Flask(__name__)

# Caminhos dos arquivos do modelo e métricas
MODEL_PATH = os.path.join("models", "model.joblib")
METRICS_PATH = os.path.join("models", "metrics.json")

# Carrega o modelo treinado
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("O arquivo 'model.joblib' não foi encontrado na pasta 'models/'.")
model = joblib.load(MODEL_PATH)

# Carrega as métricas (opcional)
if os.path.exists(METRICS_PATH):
    with open(METRICS_PATH, "r") as f:
        metrics = json.load(f)
else:
    metrics = {}

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API de predição está no ar!"})

@app.route('/metrics', methods=['GET'])
def get_metrics():
    """Retorna as métricas do modelo treinado"""
    return jsonify(metrics)

@app.route('/predict', methods=['GET'])
def predict():
    """Recebe 'size' e 'bedrooms' via query params (GET) e retorna a predição.

    Exemplo: /predict?size=120.5&bedrooms=2
    """
    try:
        # Obtém parâmetros da query string
        size_param = request.args.get("size")
        bedrooms_param = request.args.get("bedrooms")

        if size_param is None or bedrooms_param is None:
            return jsonify({"erro": "Os parâmetros 'size' e 'bedrooms' são obrigatórios na query string."}), 400

        # Conversão de tipos com validação
        try:
            size = float(size_param)
        except ValueError:
            return jsonify({"erro": "O parâmetro 'size' deve ser um número."}), 400

        try:
            # permite que o usuário passe '2' ou '2.0'
            bedrooms = int(float(bedrooms_param))
        except ValueError:
            return jsonify({"erro": "O parâmetro 'bedrooms' deve ser um inteiro."}), 400

        if size <= 0:
            return jsonify({"erro": "O parâmetro 'size' deve ser um número positivo."}), 400

        if bedrooms <= 0:
            return jsonify({"erro": "O parâmetro 'bedrooms' deve ser um inteiro positivo."}), 400

        # Faz a predição
        entrada = [[float(size), int(bedrooms)]]
        preco_previsto = model.predict(entrada)[0]

        # Retorna resultado e métrica R² (caso exista)
        return jsonify({
            "size": size,
            "bedrooms": bedrooms,
            "preco_previsto": round(float(preco_previsto), 2),
            "r2": metrics.get("r2")
        })

    except Exception as e:
        return jsonify({"erro": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)