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
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Colegio Bilingüe Monterrey</title>

            <style>
                * {{
                    box-sizing: border-box;
                }}

                body {{
                    margin: 0;
                    min-height: 100vh;
                    font-family: Arial, Helvetica, sans-serif;
                    background: linear-gradient(135deg, #2e7d32, #ff9800);
                    color: white;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    padding: 30px;
                }}

                .container {{
                    width: 100%;
                    max-width: 900px;
                    background: rgba(255, 255, 255, 0.14);
                    padding: 45px;
                    border-radius: 20px;
                    text-align: center;
                    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.30);
                }}

                h1 {{
                    font-size: 44px;
                    margin: 0 0 10px;
                }}

                h2 {{
                    color: #ffe082;
                }}

                .menu {{
                    margin-top: 30px;
                    display: flex;
                    justify-content: center;
                    flex-wrap: wrap;
                    gap: 15px;
                }}

                .menu a {{
                    min-width: 170px;
                    padding: 13px 20px;
                    border-radius: 10px;
                    background: rgba(255, 255, 255, 0.20);
                    color: white;
                    text-decoration: none;
                    font-weight: bold;
                    transition: 0.3s;
                }}

                .menu a:hover {{
                    background: white;
                    color: #2e7d32;
                    transform: translateY(-3px);
                }}

                footer {{
                    margin-top: 40px;
                    padding-top: 20px;
                    border-top: 1px solid rgba(255, 255, 255, 0.30);
                }}

                footer small {{
                    display: block;
                    margin-top: 30px;
                }}
            </style>
        </head>

        <body>
            <main class="container">
                <h1>Colegio Bilingüe Monterrey</h1>
                <h2>Portal Escolar 1</h2>

                <p>Aprendemos Juntos, Crecemos Juntos</p>

            </main>
        </body>
        </html>
        """

    @app.get("/health")
    def health():
        return jsonify(
            application="school-management-platform",
            status="healthy",
            version="1.0.0",
        ), 200

    return app


app = create_app()


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
