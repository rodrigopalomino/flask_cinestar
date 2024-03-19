from flask import Flask, jsonify, request
from flask_cors import CORS
from connector import *

# pip install flask flask_cors mysql-connector.python

app = Flask(__name__)
CORS(app)


# Cines
@app.route('/cines')
def getCines():
    # crear conexion
    conexion = connectionDB()
    # crear cursor
    cursor = conexion.cursor(dictionary=True)

    if not conexion:
        return "error al conectar base de datos"

    try:
        cursor.callproc("sp_getCines")
        cines = [row for data in cursor.stored_results()
                 for row in data.fetchall()]

        # cerrar conexion
        cursor.close()
        conexion.close()

        return cines
    except:
        return "errro en la consulta"


@app.route('/cines/<cine_id>')
def getCine(cine_id):

    # crear conexion
    conexion = connectionDB()
    # crear cursor
    cursor = conexion.cursor(dictionary=True)

    if not conexion:
        return "error al conectar base de datos"

    try:
        cursor.callproc('sp_getCine', (cine_id,))
        cine = [row for data in cursor.stored_results()
                for row in data.fetchall()]

        # cerrar conexion
        cursor.close()
        conexion.close()

        return cine[0]
    except:
        return "errro en la consulta"


@app.route('/cines/<cine_id>/tarifas')
def getCineTarifas(cine_id):
    # crear conexion
    conexion = connectionDB()
    # crear cursor
    cursor = conexion.cursor(dictionary=True)

    if not conexion:
        return "error al conectar base de datos"

    try:
        cursor.callproc('sp_getCineTarifas', (cine_id,))
        tarifas = [row for data in cursor.stored_results()
                   for row in data.fetchall()]

        # cerrar conexion
        cursor.close()
        conexion.close()

        return tarifas
    except:
        return "errro en la consulta"


@app.route('/cines/<cine_id>/peliculas')
def getCinePeliculas(cine_id):

    # crear conexion
    conexion = connectionDB()
    # crear cursor
    cursor = conexion.cursor(dictionary=True)
    if not conexion:
        return "error al conectar base de datos"

    try:
        cursor.callproc('sp_getCinePeliculas', (cine_id,))
        peliculas = [row for data in cursor.stored_results()
                     for row in data.fetchall()]

        # cerrar conexion
        cursor.close()
        conexion.close()

        return peliculas
    except:
        return "errro en la consulta"


# pelicluas
@app.route('/peliculas/<id>')
def getPeliculas(id):

    # crear conexion
    conexion = connectionDB()
    # crear cursor
    cursor = conexion.cursor(dictionary=True)

    if not conexion:
        return "error al conectar base de datos"

    try:
        id = "1" if id == "cartelera" else "2"

        cursor.callproc('sp_getPeliculas', (id,))
        peliculas = [row for data in cursor.stored_results()
                     for row in data.fetchall()]

        # cerrar conexion
        cursor.close()
        conexion.close()

        return peliculas
    except:
        return "errro en la consulta"


@app.route('/pelicula/<pelicula_id>')
def getPelicula(pelicula_id):

    # crear conexion
    conexion = connectionDB()
    # crear cursor
    cursor = conexion.cursor(dictionary=True)

    if not conexion:
        return "error al conectar base de datos"

    try:

        cursor.callproc('sp_getPelicula', (pelicula_id,))
        peliculas = [row for data in cursor.stored_results()
                     for row in data.fetchall()]

        # cerrar conexion
        cursor.close()
        conexion.close()

        return peliculas
    except:
        return "errro en la consulta"


if __name__ == '__main__':
    app.run(debug=True)
