import pytest
from flask import json
from backend.controladores.controlador_listacompras import ControladorListaCompras
from backend.app.modelos import Usuario, ListaCompra
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
        response = client.post('/v1/listas', headers=headers, data=json.dumps(data), content_type='application/json')
        assert response.status_code == 201
        assert 'Lista de compras creada exitosamente.' in response.get_json()['mensaje']
        assert ListaCompra.query.count() == 1  # Asegura que la lista haya sido creada

    def test_crear_lista_compras_sin_nombre(self, client, usuario, token):
        """ Prueba la respuesta cuando no se proporciona un nombre. """
        headers = {
            'Authorization': f'Bearer {token}'
        }
        data = {}
        response = client.post('/v1/listas', headers=headers, data=json.dumps(data), content_type='application/json')
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
        response = client.post('/v1/listas', headers={'Authorization': f'Bearer {bad_token}'}, data=json.dumps(data), content_type='application/json')
        assert response.status_code == 404
        assert 'Usuario no encontrado' in response.get_json()['error']

    def test_crear_lista_compras_sin_token(self, client):
        """ Prueba la respuesta cuando no se proporciona un token. """
        data = {'nombre': 'Groceries'}
        response = client.post('/v1/listas', data=json.dumps(data), content_type='application/json')
        assert response.status_code == 401
        assert 'Missing Authorization Header' in response.get_json()['msg']
