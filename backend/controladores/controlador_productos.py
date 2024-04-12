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

    @staticmethod
    @jwt_required()
    def consultar_productos():
        # Consultar todos los productos de la base de datos
        productos = Producto.query.all()
        # Devolver los productos en formato JSON
        return jsonify([{'id': prod.id, 'nombre': prod.nombre, 'tipo_medida': prod.tipo_medida} for prod in productos]), 200

    @staticmethod
    @jwt_required()
    def consultar_producto_por_id(productoID):
        # Consultar un producto por su ID en la base de datos
        producto = Producto.query.filter_by(id=productoID).first()
        if producto:
            # Devolver el producto en formato JSON si se encuentra
            return jsonify({'id': producto.id, 'nombre': producto.nombre, 'tipo_medida': producto.tipo_medida}), 200
        else:
            # Devolver un mensaje de error si el producto no se encuentra
            return jsonify({"error": "Producto no encontrado"}), 404

    @staticmethod
    @jwt_required()
    def actualizar_producto(productoID):
        data = request.get_json()
        producto = Producto.query.get(productoID)

        if not producto:
            return jsonify({"error": "Producto no encontrado"}), 404

        updated = False
        if 'nombre' in data:
            producto.nombre = data['nombre']
            updated = True
        if 'tipo_medida' in data:
            producto.tipo_medida = data['tipo_medida']
            updated = True

        if not updated:
            return jsonify({"error": "Ninguna propiedad provista para actualización"}), 400

        db.session.commit()
        return jsonify({"mensaje": "Producto actualizado exitosamente."}), 200

    @staticmethod
    @jwt_required()
    def eliminar_producto(productoID):
        producto = Producto.query.get(productoID)
        if not producto:
            return jsonify({"error": "Producto no encontrado"}), 404
        
        db.session.delete(producto)
        db.session.commit()
        
        return jsonify({"mensaje": "Producto eliminado exitosamente."}), 200
