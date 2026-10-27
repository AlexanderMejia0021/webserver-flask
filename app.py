from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# DataFrame con los datos del ejemplo
df = pd.DataFrame({
    "producto": ["Teclado", "Mouse", "Monitor", "Audífonos"],
    "ventas":   [12, 30, 7, 18],
    "precio":   [450, 280, 3200, 600]
})

@app.route("/")
def inicio():
    return "<h1>Servidor Flask en Codespaces</h1><p><a href='/ventas'>Ver tabla</a> | <a href='/api/ventas'>Ver JSON</a></p>"

@app.route("/ventas")
def ventas():
    return "<h1>Ventas</h1>" + df.to_html(index=False)

@app.route("/api/ventas")
def api_ventas():
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
