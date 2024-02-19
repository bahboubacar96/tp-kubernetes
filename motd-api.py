import os
from flask import Flask, jsonify

app = Flask(__name__)

# Récupérez le contenue des variables avec option valeur par defaut
message = os.environ.get('MESSAGE', 'Hello word')
app_port = int(os.environ.get('APP_PORT', 8080))

@app.route('/')
def get_motd():
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app_port)