from flask import request, jsonify
from flask_jwt_extended import create_access_token
from backend.app.modelos import db, Usuario

class ControladorUsuarios:
    @staticmethod
    def registro_usuario():
        data = request.get_json()
        nombre_usuario = data.get('nombreUsuario')
        contrasena = data.get('contrasena')
        
        if not nombre_usuario or not contrasena:
            return jsonify({"error": "Nombre de usuario y contraseña son requeridos"}), 400
        
        if Usuario.query.filter_by(nombre_usuario=nombre_usuario).first():
            return jsonify({"error": "El nombre de usuario ya está en uso"}), 409
        
        nuevo_usuario = Usuario(nombre_usuario=nombre_usuario)
        nuevo_usuario.hashear_contrasena(contrasena)
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        return jsonify({"mensaje": "Usuario creado exitosamente."}), 201

