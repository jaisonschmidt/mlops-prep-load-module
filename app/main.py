from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello World, Flask API is running!"})

if __name__ == '__main__':
    app.run(debug=True)
