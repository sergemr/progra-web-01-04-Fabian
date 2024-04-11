# /home/localadmin/progra-web-01-04-Fabian/backend/tests/modelos/test_modelo_listacompra.py
import pytest
from backend.app.modelos import ListaCompra, Usuario, db

def test_modelo_ListaCompra_tiene_todos_los_campos_correctos(session):
    # Comprueba si el modelo ListaCompra tiene todos los campos correctos
    assert hasattr(ListaCompra, 'id')
    assert hasattr(ListaCompra, 'id_usuario')
    assert hasattr(ListaCompra, 'nombre')
    assert hasattr(ListaCompra, 'estado')
    assert hasattr(ListaCompra, 'creado_en')
    assert hasattr(ListaCompra, 'actualizado_en')
    assert hasattr(ListaCompra, 'productos')

def test_creacion_ListaCompra(session):
    # Comprueba si se puede crear correctamente una ListaCompra y asociarla a un Usuario
    usuario = Usuario(nombre_usuario="testuser", hash_contrasena="testpassword")
    session.add(usuario)
    session.commit()

    lista_compra = ListaCompra(nombre="Lista de prueba", id_usuario=usuario.id)
    session.add(lista_compra)
    session.commit()

    assert lista_compra.nombre == "Lista de prueba"
    assert lista_compra.estado == "Pendiente"  # Valor por defecto
    assert lista_compra.usuario == usuario

def test_cambio_estado_ListaCompra(session):
    # Comprueba si se puede cambiar el estado de una ListaCompra
    usuario = Usuario(nombre_usuario="testuser", hash_contrasena="testpassword")
    session.add(usuario)
    session.commit()

    lista_compra = ListaCompra(nombre="Lista de prueba", id_usuario=usuario.id)
    session.add(lista_compra)
    session.commit()

    lista_compra.estado = "Completado"
    session.commit()

    assert lista_compra.estado == "Completado"

def test_eliminar_ListaCompra_cascada(session):
    # Comprueba si al eliminar un Usuario se eliminan también sus ListasCompra asociadas (prueba de cascada)
    usuario = Usuario(nombre_usuario="testuser", hash_contrasena="testpassword")
    session.add(usuario)
    session.commit()

    lista_compra = ListaCompra(nombre="Lista de prueba", id_usuario=usuario.id)
    session.add(lista_compra)
    session.commit()

    lista_compra_retrieved = session.query(ListaCompra).first()
    assert lista_compra_retrieved is not None

    session.delete(usuario)
    session.commit()

    lista_compra_retrieved = session.query(ListaCompra).first()
    assert lista_compra_retrieved is None
