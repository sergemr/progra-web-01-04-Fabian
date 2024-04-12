from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.app.modelos import db, ListaCompra, Usuario

class ControladorListaCompras:
    """
    ControladorListaCompras es una clase que maneja la creación de listas de compras para un usuario.
    """

    @staticmethod
    @jwt_required()
    def crear_lista_compras():
        """
        Crea una nueva lista de compras para un usuario.

        Retorna:
            Una respuesta JSON indicando el éxito o fracaso de la operación.
        """
        user_id = get_jwt_identity()  # Suponiendo que la identidad es el ID del usuario
        data = request.get_json()

        nombre_lista = data.get('nombre')
        if not nombre_lista:
            return jsonify({"error": "El nombre de la lista es requerido"}), 400
        
        # Obtener el usuario de la base de datos
        usuario = Usuario.query.filter_by(nombre_usuario=user_id).first()
        if not usuario:
            return jsonify({"error": "Usuario no encontrado"}), 404

        nueva_lista = ListaCompra(nombre=nombre_lista, id_usuario=usuario.id)
        db.session.add(nueva_lista)
        db.session.commit()

        return jsonify({"mensaje": "Lista de compras creada exitosamente."}), 201
