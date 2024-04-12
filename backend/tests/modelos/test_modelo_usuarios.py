import bcrypt
import pytest
from backend.app.modelos import Usuario

def test_modelo_Usuario_tiene_todos_los_campos_correctos(session):
    # Comprueba si el modelo Usuario tiene todos los campos correctos
    assert hasattr(Usuario, 'id')
    assert hasattr(Usuario, 'nombre_usuario')
    assert hasattr(Usuario, 'hash_contrasena')
    assert hasattr(Usuario, 'creado_en')
    assert hasattr(Usuario, 'actualizado_en')

def test_hashear_contrasena(session):
    # Comprueba si la función hashear_contrasena() genera un hash de contraseña válido
    usuario = Usuario()
    original_password = "testpassword"
    usuario.hashear_contrasena(original_password)
    assert usuario.hash_contrasena is not None
    assert bcrypt.checkpw(original_password.encode('utf-8'), usuario.hash_contrasena)

def test_verificar_contrasena(session):
    # Comprueba si la función verificar_contrasena() devuelve True para una contraseña correcta y False para una contraseña incorrecta
    usuario = Usuario(nombre_usuario="testuser", hash_contrasena=bcrypt.hashpw("testpassword".encode('utf-8'), bcrypt.gensalt()))
    session.add(usuario)
    session.commit()
    assert usuario.verificar_contrasena("testpassword") == True
    assert usuario.verificar_contrasena("wrongpassword") == False

def test_nombre_usuario_non_nullable(session):
    # Comprueba si se produce una excepción cuando se intenta crear un Usuario sin proporcionar un nombre de usuario
    with pytest.raises(Exception):
        usuario = Usuario(hash_contrasena="testpassword")
        session.add(usuario)
        session.commit()

def test_hash_contrasena_non_nullable(session):
    # Comprueba si se produce una excepción cuando se intenta crear un Usuario sin proporcionar un hash de contraseña
    with pytest.raises(Exception):
        usuario = Usuario(nombre_usuario="testuser")
        session.add(usuario)
        session.commit()
