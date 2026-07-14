import os

from flask import Flask, jsonify 


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        environment = os.getenv("APP_ENVIRONMENT", "development")

        return f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>School DevOps App</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 80px;">
            <h1>Proyecto Integrador DevOps</h1>
            <h2>Aplicación desplegada en Microsoft Azure</h2>
            <p>Ambiente: {environment}</p>
            <p>Versión: 1.0.0</p>
        </body>
        </html>
        """

    @app.get("/health")
    def health():
        return jsonify(
            application="school-app",
            status="healthy",
            version="1.0.0"
        ), 200

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
