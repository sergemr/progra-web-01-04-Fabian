import json
from backend.app.modelos import Usuario

class TestsRegistroUsuario:
    def test_registro_usuario_exitoso(self, client, session):
        """
        Test para verificar que un usuario se puede registrar correctamente.
        """
        nombre_usuario = "nuevoUsuario"
        contrasena = "contrasenaSegura123"
        data = {"nombreUsuario": nombre_usuario, "contrasena": contrasena}
        response = client.post("/v1/registro", data=json.dumps(data), content_type='application/json')
        assert response.status_code == 201
        assert {"mensaje": "Usuario creado exitosamente."} == response.get_json()
        usuario_creado = Usuario.query.filter_by(nombre_usuario=nombre_usuario).first()
        assert usuario_creado is not None

    def test_registro_usuario_sin_nombre_usuario(self, client, session):
        """
        Test para verificar que el registro falla si no se proporciona nombre de usuario.
        """
        data = {"contrasena": "contrasenaSegura123"}
        response = client.post("/v1/registro", data=json.dumps(data), content_type='application/json')
        assert response.status_code == 400
        assert {"error": "Nombre de usuario y contraseña son requeridos"} == response.get_json()

    def test_registro_usuario_sin_contrasena(self, client, session):
        """
        Test para verificar que el registro falla si no se proporciona contraseña.
        """
        data = {"nombreUsuario": "usuarioPrueba"}
        response = client.post("/v1/registro", data=json.dumps(data), content_type='application/json')
        assert response.status_code == 400
        assert {"error": "Nombre de usuario y contraseña son requeridos"} == response.get_json()

    def test_registro_usuario_con_nombre_existente(self, client, session):
        """
        Test para verificar que no se puede registrar un usuario con un nombre de usuario ya existente.
        """
        nombre_usuario = "usuarioExistente"
        contrasena = "contrasenaSegura"
        usuario = Usuario(nombre_usuario=nombre_usuario, hash_contrasena=contrasena)
        session.add(usuario)
        session.commit()

        data = {"nombreUsuario": nombre_usuario, "contrasena": "otraContrasena123"}
        response = client.post("/v1/registro", data=json.dumps(data), content_type='application/json')
        assert response.status_code == 409
        assert {"error": "El nombre de usuario ya está en uso"} == response.get_json()

class TestsLoginUsuario:
    def test_login_exitoso(self, client, session):
        """
        Test to verify that login is successful with valid credentials.
        """
        nombre_usuario = "usuarioValido"
        contrasena = "contrasenaValida"
        usuario = Usuario(nombre_usuario=nombre_usuario)
        usuario.hashear_contrasena(contrasena)
        session.add(usuario)
        session.commit()

        data = {"nombreUsuario": nombre_usuario, "contrasena": contrasena}
        response = client.post("/v1/login", data=json.dumps(data), content_type='application/json')

        assert response.status_code == 200
        assert "token" in response.get_json()

    def test_login_usuario_no_existente(self, client, session):
        """
        Test to verify that login fails if the user does not exist.
        """
        data = {"nombreUsuario": "usuarioNoExistente", "contrasena": "contrasenaRandom"}
        response = client.post("/v1/login", data=json.dumps(data), content_type='application/json')

        assert response.status_code == 401
        assert {"error": "Credenciales incorrectas"} == response.get_json()

    def test_login_contrasena_incorrecta(self, client, session):
        """
        Test to verify that login fails if the password is incorrect.
        """
        nombre_usuario = "usuarioValido2"
        contrasena = "contrasenaValida2"
        usuario = Usuario(nombre_usuario=nombre_usuario)
        usuario.hashear_contrasena(contrasena)
        session.add(usuario)
        session.commit()

        data = {"nombreUsuario": nombre_usuario, "contrasena": "contrasenaIncorrecta"}
        response = client.post("/v1/login", data=json.dumps(data), content_type='application/json')

        assert response.status_code == 401
        assert {"error": "Credenciales incorrectas"} == response.get_json()

    def test_login_sin_nombre_usuario(self, client, session):
        """
        Test to verify that login fails if the username is missing.
        """
        data = {"contrasena": "algunaContrasena"}
        response = client.post("/v1/login", data=json.dumps(data), content_type='application/json')

        assert response.status_code == 400
        assert {"error": "Nombre de usuario y contraseña son requeridos"} == response.get_json()

    def test_login_sin_contrasena(self, client, session):
        """
        Test to verify that login fails if the password is missing.
        """
        data = {"nombreUsuario": "usuarioPrueba"}
        response = client.post("/v1/login", data=json.dumps(data), content_type='application/json')

        assert response.status_code == 400
        assert {"error": "Nombre de usuario y contraseña son requeridos"} == response.get_json()
