import pytest
from flask import json
from backend.controladores.controlador_listacompras import ControladorListaCompras
from backend.app.modelos import Usuario, ListaCompra, Producto, ProductoLista
from flask_jwt_extended import create_access_token

class TestCrearListaCompras:
    @pytest.fixture
    def usuario(self, session):
        usuario = Usuario(nombre_usuario="testuser", hash_contrasena="hashedpassword")
        session.add(usuario)
        session.commit()
        return usuario

    @pytest.fixture
    def token(self, usuario):
        return create_access_token(identity=usuario.nombre_usuario)

    def test_crear_lista_compras_exitoso(self, client, usuario, token):
        """ Prueba la creación de una lista de compras exitosamente. """
        headers = {
            'Authorization': f'Bearer {token}'
        }
        data = {'nombre': 'Groceries'}
        response = client.post('/v1/listascompras', headers=headers, data=json.dumps(data), content_type='application/json')
        assert response.status_code == 201
        assert 'Lista de compras creada exitosamente.' in response.get_json()['mensaje']
        assert ListaCompra.query.count() == 1  # Asegura que la lista haya sido creada

    def test_crear_lista_compras_sin_nombre(self, client, usuario, token):
        """ Prueba la respuesta cuando no se proporciona un nombre. """
        headers = {
            'Authorization': f'Bearer {token}'
        }
        data = {}
        response = client.post('/v1/listascompras', headers=headers, data=json.dumps(data), content_type='application/json')
        assert response.status_code == 400
        assert 'El nombre de la lista es requerido' in response.get_json()['error']

    def test_crear_lista_compras_usuario_no_existe(self, client, token):
        """ Prueba la respuesta cuando el usuario no existe. """
        headers = {
            'Authorization': f'Bearer {token}'
        }
        data = {'nombre': 'Groceries'}
        # Simula que el usuario no existe proporcionando un token con una identidad de usuario inexistente
        bad_token = create_access_token(identity="nonexistentuser")
        response = client.post('/v1/listascompras', headers={'Authorization': f'Bearer {bad_token}'}, data=json.dumps(data), content_type='application/json')
        assert response.status_code == 404
        assert 'Usuario no encontrado' in response.get_json()['error']

    def test_crear_lista_compras_sin_token(self, client):
        """ Prueba la respuesta cuando no se proporciona un token. """
        data = {'nombre': 'Groceries'}
        response = client.post('/v1/listascompras', data=json.dumps(data), content_type='application/json')
        assert response.status_code == 401
        assert 'Missing Authorization Header' in response.get_json()['msg']

class TestAgregarProductoALista:
    @pytest.fixture
    def usuario(self, session):
        usuario = Usuario(nombre_usuario="testuser", hash_contrasena="hashedpassword")
        session.add(usuario)
        session.commit()
        return usuario

    @pytest.fixture
    def token(self, usuario):
        return create_access_token(identity=usuario.nombre_usuario)

    @pytest.fixture
    def producto(self, session):
        producto = Producto(nombre="Milk", tipo_medida="Liters")
        session.add(producto)
        session.commit()
        return producto

    @pytest.fixture
    def lista_compras(self, session, usuario):
        lista_compras = ListaCompra(nombre="Groceries", id_usuario=usuario.id)
        session.add(lista_compras)
        session.commit()
        return lista_compras

    def test_agregar_producto_a_lista_exitoso(self, client, token, lista_compras, producto):
        """ Prueba que un producto se agrega correctamente a una lista de compras. """
        headers = {
            'Authorization': f'Bearer {token}'
        }
        data = {
            'id_producto': producto.id,
            'cantidad': 2
        }
        response = client.post(f'/v1/listascompras/{lista_compras.id}/productos', headers=headers, data=json.dumps(data), content_type='application/json')
        assert response.status_code == 201
        assert 'Producto agregado exitosamente a la lista' in response.get_json()['mensaje']
        assert ProductoLista.query.count() == 1  # Asegura que el producto se ha añadido a la lista

    def test_agregar_producto_a_lista_inexistente(self, client, token, producto):
        """ Prueba agregar un producto a una lista de compras que no existe. """
        headers = {
            'Authorization': f'Bearer {token}'
        }
        data = {
            'id_producto': producto.id,
            'cantidad': 2
        }
        response = client.post('/v1/listascompras/999/products', headers=headers, data=json.dumps(data), content_type='application/json')
        assert response.status_code == 404

    def test_agregar_producto_no_existente_a_lista(self, client, token, lista_compras):
        """ Prueba agregar un producto que no existe a una lista de compras. """
        headers = {
            'Authorization': f'Bearer {token}'
        }
        data = {
            'id_producto': 999,
            'cantidad': 2
        }
        response = client.post(f'/v1/listascompras/{lista_compras.id}/productos', headers=headers, data=json.dumps(data), content_type='application/json')
        assert response.status_code == 404

    def test_agregar_producto_a_lista_datos_incompletos(self, client, token, lista_compras):
        """ Prueba agregar un producto a una lista con datos incompletos. """
        headers = {
            'Authorization': f'Bearer {token}'
        }
        data = {'cantidad': 3}  # falta id_producto
        response = client.post(f'/v1/listascompras/{lista_compras.id}/productos', headers=headers, data=json.dumps(data), content_type='application/json')
        assert response.status_code == 400
        assert 'Información proporcionada inválida o incompleta' in response.get_json()['error']

    def test_agregar_producto_a_lista_sin_token(self, client, lista_compras, producto):
        """ Prueba agregar un producto a una lista sin proporcionar token de autenticación. """
        data = {
            'id_producto': producto.id,
            'cantidad': 2
        }
        response = client.post(f'/v1/listascompras/{lista_compras.id}/productos', data=json.dumps(data), content_type='application/json')
        assert response.status_code == 401
        assert 'Missing Authorization Header' in response.get_json()['msg']
