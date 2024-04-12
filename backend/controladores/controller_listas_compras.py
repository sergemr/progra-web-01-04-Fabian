# # /home/localadmin/progra-web-01-04-Fabian/backend/controllers/controller_listas_compras.py

# from flask import request, jsonify
# from backend.app.modelos import ListaProducto, Producto, db, ListaCompra, Usuario
# # Make sure to import Usuario if you need to validate the user

# class ListasComprasController:
#     @staticmethod
#     def crear_lista_compras():
#         data = request.get_json()
#         nombre_lista = data.get('nombre')
#         usuario_id = data.get('usuario_id')  # Assuming you're passing user ID in the request

#         if not nombre_lista or not usuario_id:
#             return jsonify({"error": "Nombre de la lista y ID del usuario son requeridos"}), 400
        
#         # Optional: Validate if user exists
#         usuario = Usuario.query.get(usuario_id)
#         if usuario is None:
#             return jsonify({"error": "Usuario no encontrado"}), 404

#         nueva_lista = ListaCompra(nombre=nombre_lista, usuario_id=usuario_id)
#         db.session.add(nueva_lista)
#         try:
#             db.session.commit()
#             return jsonify({"mensaje": "Lista de compras creada con éxito", "lista_id": nueva_lista.id}), 201
#         except Exception as e:
#             db.session.rollback()
#             return jsonify({"error": f"Error al crear la lista de compras: {e}"}), 500

#     @staticmethod
#     def agregar_producto_a_lista(id_lista):
#         data = request.get_json()
#         producto_id = data.get('producto_id')
#         cantidad = data.get('cantidad')

#         if not producto_id or not cantidad:
#             return jsonify({"error": "Producto ID y cantidad son requeridos"}), 400

#         lista_compra = ListaCompra.query.get(id_lista)
#         if lista_compra is None:
#             return jsonify({"error": "Lista de compras no encontrada"}), 404

#         producto = Producto.query.get(producto_id)
#         if producto is None:
#             return jsonify({"error": "Producto no encontrado"}), 404

#         nuevo_producto_lista = ListaProducto(lista_compra_id=id_lista, producto_id=producto_id, cantidad=cantidad)
#         db.session.add(nuevo_producto_lista)
#         try:
#             db.session.commit()
#             return jsonify({"mensaje": "Producto agregado a la lista de compras con éxito"}), 201
#         except Exception as e:
#             db.session.rollback()
#             return jsonify({"error": f"Error al agregar producto a la lista de compras: {e}"}), 500

#     @staticmethod
#     def ver_lista_compras(id_lista):
#         try:
#             lista_compra = ListaCompra.query.get(id_lista)
#             if lista_compra is None:
#                 return jsonify({"error": "Lista de compras no encontrada"}), 404

#             productos = []
#             for producto in lista_compra.productos:
#                 prod_details = {
#                     "producto_id": producto.producto.id,
#                     "nombre": producto.producto.nombre,
#                     "cantidad": str(producto.cantidad),
#                     "unidad_medida": producto.producto.unidad_medida,
#                     "imagen": producto.producto.imagen,
#                     "comprado": producto.producto.comprado
#                 }
#                 productos.append(prod_details)

#             lista_details = {
#                 "lista_id": lista_compra.id,
#                 "nombre": lista_compra.nombre,
#                 "fecha_creacion": lista_compra.fecha_creacion.isoformat(),
#                 "productos": productos
#             }

#             return jsonify(lista_details), 200
#         except Exception as e:
#             # Log the exception details here, if logging is set up
#             return jsonify({"error": f"Error al recuperar la lista de compras: {str(e)}"}), 500
    
#     # Add this method to the ListasComprasController class in controller_listas_compras.py
#     @staticmethod
#     def listar_todas_listas_usuario(id_usuario):
#         try:
#             usuario = Usuario.query.get(id_usuario)
#             if usuario is None:
#                 return jsonify({"error": "Usuario no encontrado"}), 404
            
#             listas = ListaCompra.query.filter_by(usuario_id=id_usuario).all()
#             listas_data = []
#             for lista in listas:
#                 listas_data.append({
#                     "lista_id": lista.id,
#                     "nombre": lista.nombre,
#                     "fecha_creacion": lista.fecha_creacion.isoformat(),
#                     # Additional details can be added here as needed
#                 })
            
#             return jsonify(listas_data), 200
#         except Exception as e:
#             # It's a good practice to log the error here
#             return jsonify({"error": f"Error al recuperar las listas de compras: {str(e)}"}), 500
