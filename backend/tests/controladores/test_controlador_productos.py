import json
from backend.app.modelos import Producto
from flask_jwt_extended import create_access_token

class TestsAgregarProducto:
    def test_agregar_producto_exitoso(self, client, session):
        """
        Prueba para verificar que se pueda agregar un producto exitosamente con credenciales válidas y datos completos.
        """
        # Configuración: crear un usuario y obtener un token válido
        user_id = "testUser"
        token = create_access_token(identity=user_id)
        headers = {
            'Authorization': f'Bearer {token}'
        }
        data = {"nombre": "Cafe", "tipo_medida": "Kilogramos"}
        response = client.post("/v1/productos", data=json.dumps(data), headers=headers, content_type='application/json')
        assert response.status_code == 201
        assert {"mensaje": "Producto agregado exitosamente."} == response.get_json()
        assert Producto.query.count() == 1  # Asegurar que el producto se agregue a la base de datos

    def test_agregar_producto_falla_sin_datos(self, client, session):
        """
        Prueba para asegurar que la adición de producto falle cuando faltan campos de datos requeridos.
        """
        user_id = "testUser"
        token = create_access_token(identity=user_id)
        headers = {
            'Authorization': f'Bearer {token}'
        }
        data = {}  # Faltan tanto 'nombre' como 'tipo_medida'
        response = client.post("/v1/productos", data=json.dumps(data), headers=headers, content_type='application/json')
        assert response.status_code == 400
        assert {"error": "Información proporcionada inválida o incompleta"} == response.get_json()

    def test_agregar_producto_falla_sin_autenticacion(self, client, session):
        """
        Prueba para verificar que la adición de producto falle sin autenticación JWT.
        """
        data = {"nombre": "Cafe", "tipo_medida": "Kilogramos"}
        response = client.post("/v1/productos", data=json.dumps(data), content_type='application/json')
        assert response.status_code == 401  # Verificar el código de estado no autorizado

    def test_agregar_producto_falla_con_campos_incompletos(self, client, session):
        """
        Prueba para asegurar que la adición de producto falle cuando falta algún campo requerido.
        """
        user_id = "testUser"
        token = create_access_token(identity=user_id)
        headers = {
            'Authorization': f'Bearer {token}'
        }
        data = {"nombre": "Cafe"}  # Falta 'tipo_medida'
        response = client.post("/v1/productos", data=json.dumps(data), headers=headers, content_type='application/json')
        assert response.status_code == 400
        assert {"error": "Información proporcionada inválida o incompleta"} == response.get_json()

class TestsConsultarProductos:
    def test_consultar_productos_exitoso(self, client, session):
        """
        Test para verificar que se pueda consultar la lista de productos correctamente.
        """
        # Configuración: crear productos y obtener un token válido
        user_id = "testUser"
        token = create_access_token(identity=user_id)
        headers = {
            'Authorization': f'Bearer {token}'
        }
        # Agregar productos de prueba a la base de datos
        producto1 = Producto(nombre="Producto1", tipo_medida="Unidades")
        producto2 = Producto(nombre="Producto2", tipo_medida="Litros")
        session.add(producto1)
        session.add(producto2)
        session.commit()

        # Realizar la petición
        response = client.get("/v1/productos", headers=headers)
        assert response.status_code == 200
        productos_response = response.get_json()
        assert len(productos_response) == 2
        assert productos_response[0]['nombre'] == "Producto1"
        assert productos_response[1]['nombre'] == "Producto2"

    def test_consultar_productos_vacia(self, client, session):
        """
        Test para verificar el comportamiento cuando no hay productos en la base de datos.
        """
        user_id = "testUser"
        token = create_access_token(identity=user_id)
        headers = {
            'Authorization': f'Bearer {token}'
        }

        response = client.get("/v1/productos", headers=headers)
        assert response.status_code == 200
        productos_response = response.get_json()
        assert productos_response == []

    def test_consultar_productos_sin_autenticacion(self, client):
        """
        Test para verificar que la consulta de productos requiere autenticación.
        """
        response = client.get("/v1/productos")
        assert response.status_code == 401

class TestsConsultarProductoPorID:
    def test_consultar_producto_por_id_exitoso(self, client, session):
        """
        Prueba para verificar que se puede consultar un producto por su ID correctamente.
        """
        # Setup: Crear un producto y obtener un token válido
        producto = Producto(nombre="Cafe", tipo_medida="Kilogramos")
        session.add(producto)
        session.commit()
        
        user_id = "testUser"
        token = create_access_token(identity=user_id)
        headers = {
            'Authorization': f'Bearer {token}'
        }
        
        # Action: Consultar el producto
        response = client.get(f"/v1/productos/{producto.id}", headers=headers)
        
        # Verification
        assert response.status_code == 200
        expected_data = {'id': producto.id, 'nombre': producto.nombre, 'tipo_medida': producto.tipo_medida}
        assert response.get_json() == expected_data

    def test_producto_no_encontrado(self, client, session):
        """
        Prueba para verificar que se devuelve un error cuando el ID del producto no existe.
        """
        user_id = "testUser"
        token = create_access_token(identity=user_id)
        headers = {
            'Authorization': f'Bearer {token}'
        }
        
        # Action: Consultar un producto con ID inexistente
        response = client.get("/v1/productos/999", headers=headers)
        
        # Verification
        assert response.status_code == 404
        assert {"error": "Producto no encontrado"} == response.get_json()

    def test_consultar_producto_sin_autenticacion(self, client, session):
        """
        Prueba para verificar que la consulta de producto falla sin autenticación JWT.
        """
        response = client.get("/v1/productos/1")
        assert response.status_code == 401
        assert "msg" in response.get_json()  # Assuming Flask-JWT-Extended default error messages

    def test_consultar_producto_con_token_invalido(self, client, session):
        """
        Prueba para verificar que la consulta de producto falla con un token JWT inválido.
        """
        headers = {
            'Authorization': 'Bearer invalidtokenhere'
        }
        response = client.get("/v1/productos/1", headers=headers)
        assert response.status_code == 422  # Assuming Flask-JWT-Extended default status code for invalid tokens

class TestsActualizarProducto:
    def test_actualizar_producto_exitoso(self, client, session):
        """
        Test para verificar que un producto se puede actualizar correctamente con todos los campos necesarios.
        """
        # Crear un producto en la base de datos para actualizarlo
        producto_original = Producto(nombre="Leche", tipo_medida="Litros")
        session.add(producto_original)
        session.commit()
        
        # Configuración: crear un usuario y obtener un token válido
        user_id = "testUser"
        token = create_access_token(identity=user_id)
        headers = {'Authorization': f'Bearer {token}'}
        
        # Datos de actualización
        data = {"nombre": "Leche Modificada", "tipo_medida": "Litros"}
        response = client.put(f"/v1/productos/{producto_original.id}", data=json.dumps(data), headers=headers, content_type='application/json')
        assert response.status_code == 200
        assert {"mensaje": "Producto actualizado exitosamente."} == response.get_json()
        
        # Verificar cambios en la base de datos
        producto_actualizado = Producto.query.get(producto_original.id)
        assert producto_actualizado.nombre == "Leche Modificada"

    def test_actualizar_solo_nombre_producto(self, client, session):
        """
        Test para verificar que se puede actualizar solo el nombre del producto.
        """
        producto = Producto(nombre="Cereal", tipo_medida="Cajas")
        session.add(producto)
        session.commit()
        
        user_id = "testUser"
        token = create_access_token(identity=user_id)
        headers = {'Authorization': f'Bearer {token}'}
        
        # Actualizar solo el nombre
        data = {"nombre": "Cereal Actualizado"}
        response = client.put(f"/v1/productos/{producto.id}", data=json.dumps(data), headers=headers, content_type='application/json')
        assert response.status_code == 200
        assert {"mensaje": "Producto actualizado exitosamente."} == response.get_json()
        
        # Verificar que solo el nombre haya cambiado
        producto_actualizado = Producto.query.get(producto.id)
        assert producto_actualizado.nombre == "Cereal Actualizado"
        assert producto_actualizado.tipo_medida == "Cajas"  # Asegurarse que el tipo de medida no cambió

    def test_actualizar_solo_tipo_medida(self, client, session):
        """
        Test para verificar que se puede actualizar solo el tipo de medida del producto.
        """
        producto = Producto(nombre="Pan", tipo_medida="Unidades")
        session.add(producto)
        session.commit()
        
        user_id = "testUser"
        token = create_access_token(identity=user_id)
        headers = {'Authorization': f'Bearer {token}'}
        
        # Actualizar solo el tipo de medida
        data = {"tipo_medida": "Docenas"}
        response = client.put(f"/v1/productos/{producto.id}", data=json.dumps(data), headers=headers, content_type='application/json')
        assert response.status_code == 200
        assert {"mensaje": "Producto actualizado exitosamente."} == response.get_json()
        
        # Verificar que solo el tipo de medida haya cambiado
        producto_actualizado = Producto.query.get(producto.id)
        assert producto_actualizado.nombre == "Pan"  # Asegurarse que el nombre no cambió
        assert producto_actualizado.tipo_medida == "Docenas"

    def test_actualizar_producto_no_existente(self, client, session):
        """
        Prueba para verificar que la actualización falla si el producto no existe.
        """
        user_id = "testUser"
        token = create_access_token(identity=user_id)
        headers = {'Authorization': f'Bearer {token}'}
        
        data = {"nombre": "Producto Fantasma", "tipo_medida": "Kilos"}
        response = client.put("/v1/productos/99999", data=json.dumps(data), headers=headers, content_type='application/json')
        assert response.status_code == 404
        assert {"error": "Producto no encontrado"} == response.get_json()

    def test_actualizar_producto_falla_sin_cambios(self, client, session):
        """
        Prueba para asegurar que la actualización falla cuando no se proporcionan campos para actualizar.
        """
        producto = Producto(nombre="Azúcar", tipo_medida="Kilos")
        session.add(producto)
        session.commit()
        
        user_id = "testUser"
        token = create_access_token(identity=user_id)
        headers = {'Authorization': f'Bearer {token}'}
        
        data = {}  # No se proporcionan campos para actualizar
        response = client.put(f"/v1/productos/{producto.id}", data=json.dumps(data), headers=headers, content_type='application/json')
        assert response.status_code == 400
        assert {"error": "Ninguna propiedad provista para actualización"} == response.get_json()

    def test_actualizar_producto_falla_sin_autenticacion(self, client):
        """
        Prueba para verificar que la actualización de producto falle sin autenticación JWT.
        """
        data = {"nombre": "Cafe", "tipo_medida": "Kilogramos"}
        response = client.put("/v1/productos/1", data=json.dumps(data), content_type='application/json')
        assert response.status_code == 401  # Verificar el código de estado no autorizado

class TestsEliminarProducto:
    def test_eliminar_producto_exitoso(self, client, session):
        """
        Test para verificar que un producto se puede eliminar correctamente.
        """
        # Configuración: crear un producto en la base de datos
        producto = Producto(nombre="ProductoEliminar", tipo_medida="Unidades")
        session.add(producto)
        session.commit()

        # Obtener un token válido
        user_id = "testUser"
        token = create_access_token(identity=user_id)
        headers = {'Authorization': f'Bearer {token}'}

        # Eliminar el producto
        response = client.delete(f"/v1/productos/{producto.id}", headers=headers)

        # Verificar que la respuesta y el estado de la base de datos son correctos
        assert response.status_code == 200
        assert {"mensaje": "Producto eliminado exitosamente."} == response.get_json()
        assert Producto.query.get(producto.id) is None  # El producto no debe existir en la base de datos

    def test_eliminar_producto_no_existente(self, client, session):
        """
        Test para verificar que se devuelve un error cuando se intenta eliminar un producto que no existe.
        """
        # Obtener un token válido
        user_id = "testUser"
        token = create_access_token(identity=user_id)
        headers = {'Authorization': f'Bearer {token}'}

        # Intentar eliminar un producto con un ID que no existe
        response = client.delete("/v1/productos/99999", headers=headers)

        # Verificar que se devuelve un mensaje de error adecuado
        assert response.status_code == 404
        assert {"error": "Producto no encontrado"} == response.get_json()

    def test_eliminar_producto_sin_autenticacion(self, client):
        """
        Test para verificar que la eliminación de un producto requiere autenticación.
        """
        # Intentar eliminar un producto sin proporcionar token de autenticación
        response = client.delete("/v1/productos/1")

        # Verificar que se requiere autenticación
        assert response.status_code == 401
        assert "msg" in response.get_json()  # Suponiendo que Flask-JWT-Extended usa mensajes de error predeterminados
