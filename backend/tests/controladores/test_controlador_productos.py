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
