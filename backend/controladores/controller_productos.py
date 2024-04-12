# from flask import request, jsonify
# from backend.app.modelos import db, Producto

# class ProductosController:
#     @staticmethod
#     def agregar_producto():
#         print("Inicio del proceso para agregar un producto.")
#         data = request.get_json()
        
#         nombre = data.get('nombre')
#         cantidad = data.get('cantidad')
#         unidad_medida = data.get('unidad_medida')
#         imagen = data.get('imagen', None)  # Optional
#         comprado = data.get('comprado', False)  # Default to False if not provided
        
#         if not all([nombre, cantidad, unidad_medida]):
#             print("Error: Faltan datos requeridos para agregar el producto.")
#             return jsonify({"error": "Faltan datos requeridos: nombre, cantidad, unidad_medida"}), 400
        
#         print(f"Agregando producto: {nombre}, Cantidad: {cantidad}, Unidad: {unidad_medida}, Imagen: {imagen}, Comprado: {comprado}")
        
#         nuevo_producto = Producto(nombre=nombre, cantidad=cantidad, unidad_medida=unidad_medida, imagen=imagen, comprado=comprado)
#         db.session.add(nuevo_producto)
        
#         try:
#             db.session.commit()
#             print("Producto agregado con éxito.")
#             return jsonify({"mensaje": "Producto agregado con éxito", "producto_id": nuevo_producto.id}), 201
#         except Exception as e:
#             print(f"Error al intentar agregar el producto a la base de datos: {e}")
#             db.session.rollback()
#             return jsonify({"error": f"Error al agregar producto: {e}"}), 500

#     @staticmethod
#     def listar_todos_los_productos():
#         try:
#             # Query all products
#             productos = Producto.query.all()
#             # Convert product objects to a list of dictionaries
#             lista_productos = [{
#                 'id': producto.id,
#                 'nombre': producto.nombre,
#                 'cantidad': producto.cantidad,
#                 'unidad_medida': producto.unidad_medida,
#                 'imagen': producto.imagen,
#                 'comprado': producto.comprado
#             } for producto in productos]

#             return jsonify(lista_productos), 200
#         except Exception as e:
#             print(f"Error retrieving products: {e}")
#             return jsonify({"error": "Error al recuperar los productos de la base de datos"}), 500