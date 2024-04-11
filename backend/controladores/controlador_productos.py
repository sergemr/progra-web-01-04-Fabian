from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from backend.app.modelos import db, Producto

class ControladorProductos:
    @staticmethod
    @jwt_required()
    def agregar_producto():
        user_id = get_jwt_identity()
        data = request.get_json()
        
        # Validación básica
        if 'nombre' not in data or 'tipo_medida' not in data:
            return jsonify({"error": "Información proporcionada inválida o incompleta"}), 400
        
        # Crear una nueva instancia de Producto
        nuevo_producto = Producto(
            nombre=data['nombre'],
            tipo_medida=data['tipo_medida']
        )
        
        # Agregar a la base de datos
        db.session.add(nuevo_producto)
        db.session.commit()
        
        return jsonify({"mensaje": "Producto agregado exitosamente."}), 201
