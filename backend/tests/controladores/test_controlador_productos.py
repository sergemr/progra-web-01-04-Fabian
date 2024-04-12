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
