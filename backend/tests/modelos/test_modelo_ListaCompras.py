# from datetime import datetime, timezone
# from backend.app.modelos import db, ListaCompra, Usuario
# import pytest

# def create_usuario(session, nombre='Test Usuario', contrasenha='password'):
#     """
#     Helper function to create a user with default or specified attributes.
#     """
#     new_usuario = Usuario(nombre=nombre, contrasenha=contrasenha)
#     session.add(new_usuario)
#     session.commit()
#     return new_usuario

# def create_lista_compra(session, usuario_id, nombre='Lista de Compra Default', fecha_creacion=datetime.now(timezone.utc)):
#     """
#     Helper function to create a shopping list with default or specified attributes.
#     """
#     new_lista_compra = ListaCompra(usuario_id=usuario_id, nombre=nombre, fecha_creacion=fecha_creacion)
#     session.add(new_lista_compra)
#     session.commit()
#     return new_lista_compra

# @pytest.fixture
# def usuario_default(session):
#     """
#     Pytest fixture to create a default user for tests.
#     """
#     return create_usuario(session)

# def test_create_lista_compra(app, session, usuario_default):
#     with app.app_context():
#         usuario_id = usuario_default.id
#         create_lista_compra(session, usuario_id, 'Lista Test')

#         lista_compra = ListaCompra.query.filter_by(nombre='Lista Test').first()
#         assert lista_compra is not None
#         assert lista_compra.usuario_id == usuario_id
#         assert lista_compra.nombre == 'Lista Test'

# def test_read_lista_compra(app, session, usuario_default):
#     with app.app_context():
#         usuario_id = usuario_default.id
#         nombre_lista = 'Lista para Leer'
#         create_lista_compra(session, usuario_id, nombre_lista)

#         lista_compra = ListaCompra.query.filter_by(nombre=nombre_lista).first()
#         assert lista_compra is not None
#         assert lista_compra.nombre == nombre_lista

# def test_update_lista_compra(app, session, usuario_default):
#     with app.app_context():
#         usuario_id = usuario_default.id
#         lista_compra = create_lista_compra(session, usuario_id)  # Use default name and date

#         lista_compra.nombre = 'Lista Actualizada'
#         session.commit()

#         updated_lista = ListaCompra.query.filter_by(nombre='Lista Actualizada').first()
#         assert updated_lista is not None
#         assert updated_lista.nombre == 'Lista Actualizada'

# def test_delete_lista_compra(app, session, usuario_default):
#     with app.app_context():
#         usuario_id = usuario_default.id
#         nombre_lista = 'Lista para Borrar'
#         create_lista_compra(session, usuario_id, nombre_lista)

#         lista_compra = ListaCompra.query.filter_by(nombre=nombre_lista).first()
#         session.delete(lista_compra)
#         session.commit()

#         deleted_lista = ListaCompra.query.filter_by(nombre=nombre_lista).first()
#         assert deleted_lista is None
