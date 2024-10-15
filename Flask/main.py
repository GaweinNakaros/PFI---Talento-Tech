from flask import Flask, jsonify , request

app = Flask(__name__) # Definimos el nombre de la app 

@app.route("/")
def root():
    return "Home"

"""

Get -> Obtener Informacion
Post -> Crear Informacion
Put -> Actualizar Infromacion
Delete -> Borrar Informacion

"""

# Inicio del Servidor

if __name__ == "__name__":
    app.run(debug=True)
