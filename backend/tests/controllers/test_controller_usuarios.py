# # Import necessary libraries and modules
# import pytest
# from backend.app.modelos import Usuario

# # Helper function to add a user to the database
# def add_user(session, username, password):
#     user = Usuario(nombre=username, contrasenha=password)
#     session.add(user)
#     session.commit()

# class TestUsuariosController:
#     # Test case for successful user registration
#     def test_successful_user_registration(self, client, session):
#         response = client.post('/api/usuarios', json={'nombre_usuario': 'testuser', 'contrasenha': 'testpass'})
#         assert response.status_code == 201
#         assert 'Usuario registrado con éxito' in response.get_json()['mensaje']

#     # Test case for registration with missing username or password
#     @pytest.mark.parametrize("payload", [
#         {'nombre_usuario': 'testuser'},  # Missing password
#         {'contrasenha': 'testpass'},  # Missing username
#         {}  # Missing both
#     ])
#     def test_registration_with_missing_credentials(self, client, payload):
#         response = client.post('/api/usuarios', json=payload)
#         assert response.status_code == 400
#         assert 'Nombre de usuario y contraseña son requeridos' in response.get_json()['error']

#     # Test case for attempting to register a duplicate user
#     def test_duplicate_user_registration(self, client, session):
#         add_user(session, 'testuser', 'testpass')
#         response = client.post('/api/usuarios', json={'nombre_usuario': 'testuser', 'contrasenha': 'newpass'})
#         assert response.status_code == 409
#         assert 'El usuario ya existe' in response.get_json()['error']

#     # Test case for successful login
#     def test_successful_login(self, client, session):
#         add_user(session, 'loginuser', 'loginpass')
#         response = client.post('/api/usuarios/login', json={'nombre_usuario': 'loginuser', 'contrasenha': 'loginpass'})
#         assert response.status_code == 200
#         assert 'Inicio de sesión exitoso' in response.get_json()['mensaje']

#     # Test case for login with incorrect credentials
#     def test_login_with_incorrect_credentials(self, client, session):
#         add_user(session, 'user1', 'pass1')
#         response = client.post('/api/usuarios/login', json={'nombre_usuario': 'user1', 'contrasenha': 'wrongpass'})
#         assert response.status_code == 401
#         assert 'Credenciales incorrectas' in response.get_json()['error']

#     # Test case for login with missing username or password
#     @pytest.mark.parametrize("payload", [
#         {'nombre_usuario': 'user'},  # Missing password
#         {'contrasenha': 'pass'},  # Missing username
#         {}  # Missing both
#     ])
#     def test_login_with_missing_credentials(self, client, payload):
#         response = client.post('/api/usuarios/login', json=payload)
#         assert response.status_code == 400
#         assert 'Nombre de usuario y contraseña son requeridos' in response.get_json()['error']