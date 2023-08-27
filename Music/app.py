import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuración de la conexión a la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'musica'
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

@app.route('/canciones', methods=['POST'])
def crear_cancion():
    data = request.json
    query = "INSERT INTO Cancion (id, titulo, minutos, segundos, interprete) VALUES (%s, %s, %s, %s, %s)"
    values = (data['id'], data['titulo'], data['minutos'], data['segundos'], data['interprete'])

    cursor.execute(query, values)
    connection.commit()

    return "Canción creada exitosamente", 201

@app.route('/canciones', methods=['GET'])
def obtener_canciones():
    query = "SELECT * FROM Cancion"

    cursor.execute(query)
    canciones = cursor.fetchall()

    canciones_list = []
    for cancion in canciones:
        cancion_dict = {
            'id': cancion[0],
            'titulo': cancion[1],
            'minutos': cancion[2],
            'segundos': cancion[3],
            'interprete': cancion[4]
        }
        canciones_list.append(cancion_dict)

    return jsonify(canciones_list)

@app.route('/canciones/<int:cancion_id>', methods=['PUT'])
def actualizar_cancion(cancion_id):
    data = request.json
    query = "UPDATE Cancion SET titulo=%s, minutos=%s, segundos=%s, interprete=%s WHERE id=%s"
    values = (data['titulo'], data['minutos'], data['segundos'], data['interprete'], cancion_id)

    cursor.execute(query, values)
    connection.commit()

    return "Canción actualizada exitosamente"

@app.route('/canciones/<int:cancion_id>', methods=['DELETE'])
def eliminar_cancion(cancion_id):
    query = "DELETE FROM Cancion WHERE id=%s"
    values = (cancion_id,)

    cursor.execute(query, values)
    connection.commit()

    return "Canción eliminada exitosamente"

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.json
    query = "INSERT INTO Usuario (id, nombre, contrasena) VALUES (%s, %s, %s)"
    values = (data['id'], data['nombre'], data['contrasena'])

    cursor.execute(query, values)
    connection.commit()

    return "Usuario creado exitosamente", 201

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    query = "SELECT * FROM Usuario"

    cursor.execute(query)
    usuarios = cursor.fetchall()

    usuarios_list = []
    for usuario in usuarios:
        usuario_dict = {
            'id': usuario[0],
            'nombre': usuario[1],
            'contrasena': usuario[2]
        }
        usuarios_list.append(usuario_dict)

    return jsonify(usuarios_list)

@app.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def actualizar_usuario(usuario_id):
    data = request.json
    query = "UPDATE Usuario SET nombre=%s, contrasena=%s WHERE id=%s"
    values = (data['nombre'], data['contrasena'], usuario_id)

    cursor.execute(query, values)
    connection.commit()

    return "Usuario actualizado exitosamente"

@app.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def eliminar_usuario(usuario_id):
    query = "DELETE FROM Usuario WHERE id=%s"
    values = (usuario_id,)

    cursor.execute(query, values)
    connection.commit()

    return "Usuario eliminado exitosamente"

@app.route('/albumes', methods=['POST'])
def crear_album():
    data = request.json
    query = "INSERT INTO Album (id, titulo, anio, descripcion, usuario) VALUES (%s, %s, %s, %s, %s)"
    values = (data['id'], data['titulo'], data['anio'], data['descripcion'], data['usuario'])

    cursor.execute(query, values)
    connection.commit()

    return "Álbum creado exitosamente", 201

@app.route('/albumes', methods=['GET'])
def obtener_albumes():
    query = "SELECT * FROM Album"

    cursor.execute(query)
    albumes = cursor.fetchall()

    albumes_list = []
    for album in albumes:
        album_dict = {
            'id': album[0],
            'titulo': album[1],
            'anio': album[2],
            'descripcion': album[3],
            'usuario': album[4]
        }
        albumes_list.append(album_dict)

    return jsonify(albumes_list)

@app.route('/albumes/<int:album_id>', methods=['PUT'])
def actualizar_album(album_id):
    data = request.json
    query = "UPDATE Album SET titulo=%s, anio=%s, descripcion=%s, usuario=%s WHERE id=%s"
    values = (data['titulo'], data['anio'], data['descripcion'], data['usuario'], album_id)

    cursor.execute(query, values)
    connection.commit()

    return "Álbum actualizado exitosamente"

@app.route('/albumes/<int:album_id>', methods=['DELETE'])
def eliminar_album(album_id):
    query = "DELETE FROM Album WHERE id=%s"
    values = (album_id,)

    cursor.execute(query, values)
    connection.commit()

    return "Álbum eliminado exitosamente"

@app.route('/albumes/<int:album_id>/canciones/<int:cancion_id>', methods=['POST'])
def agregar_cancion_a_album(album_id, cancion_id):
    query = "INSERT INTO Album_Cancion (album_id, cancion_id) VALUES (%s, %s)"
    values = (album_id, cancion_id)

    cursor.execute(query, values)
    connection.commit()

    return "Canción agregada al álbum exitosamente", 201

@app.route('/albumes/<int:album_id>/canciones/<int:cancion_id>', methods=['DELETE'])
def eliminar_cancion_de_album(album_id, cancion_id):
    query = "DELETE FROM Album_Cancion WHERE album_id=%s AND cancion_id=%s"
    values = (album_id, cancion_id)

    cursor.execute(query, values)
    connection.commit()

    return "Canción eliminada del álbum exitosamente"



if __name__ == '__main__':
    app.run()


