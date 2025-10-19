from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    app_name = os.getenv("APP_NAME", "Mi App Flask en Kubernetes")
    return f"<h1>{app_name}</h1><p>¡Desplegada correctamente en Kubernetes con Minikube!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
