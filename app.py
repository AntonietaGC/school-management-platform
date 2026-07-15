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
                
                 .modal {{
        	     display: none;
                     position: fixed;
                     inset: 0;
                     background: rgba(0,0,0,.65);
                     justify-content: center;
                     align-items: center;
                     z-index: 1000;
                 }}

                 .modal-content {{
                     position: relative;
                     background: white;
                     color: #333;
                     padding: 35px;
                     border-radius: 15px;
                     width: 450px;
                     text-align: center;
                     box-shadow: 0 10px 30px rgba(0,0,0,.4);
                 }}

                 .modal-content h2 {{
                     color: #2e7d32;
                 }}

                 .close-button {{
                     position: absolute;
                     top: 10px;
                     right: 15px;
                     background: transparent;
                     border: none;
                     font-size: 28px;
                     cursor: pointer;
                  }}

                .return-button {{
                    margin-top: 20px;
                    background: #ff9800;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 8px;
                    cursor: pointer;
                    font-size: 16px;
                  }}

                .return-button:hover {{
                    background: #e68900;
                  }}

            </style>
        </head>

        <body>
            <main class="container">
                <h1>Colegio Bilingüe Monterrey</h1>
                <h2>Portal Escolar 1</h2>

                <p>Aprendemos Juntos, Crecemos Juntos</p>

                <p>Seleccione una opción</p>

                <nav class="menu">
                    <a href="#">Login / Register</a>
                    <a href="#">Learning Plan</a>
                    <a href="#">Library</a>
                    <a href="#">Calendar</a>
                    <a href="#" onclick="openContact(); return false;"> Contact</a>
                </nav> 

                  <footer>
                    <h3>Nuestra misión</h3>

                    <p>
                        Formar estudiantes íntegros, bilingües e innovadores,
                        promoviendo la excelencia académica y el uso responsable
                        de la tecnología.
                    </p>

                    <small>
                        © 2026 Colegio Bilingüe Monterrey |
                        Ambiente: {environment}
                   </small>
                </footer>

             <div id="contactModal" class="modal">
                 <div class="modal-content">
                     <button class="close-button" onclick="closeContact()">
                        &times;
                     </button>

                     <h2>Contacto</h2>

                     <p><strong>Colegio Bilingüe Monterrey</strong></p>
                     <p>📍 Monterrey, Nuevo León</p>
                     <p>📞 Teléfono: (81) 5555-2026</p>
                     <p>✉ Correo: contacto@colegiomonterrey.edu</p>
                     <p>🕒 Horario: lunes a viernes, 8:00 a.m. a 4:00 p.m.</p>

                     <button class="return-button" onclick="closeContact()">
                         Volver al menú
                     </button>
                 </div>
              </div>
            </main>
          <script>
              function openContact() {{
                  document.getElementById("contactModal").style.display = "flex";
              }}

              function closeContact() {{
                  document.getElementById("contactModal").style.display = "none";
              }}

              window.onclick = function(event) {{
                  const modal = document.getElementById("contactModal");

                  if (event.target === modal) {{
                      closeContact();
                  }}
              }};
          </script>
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
