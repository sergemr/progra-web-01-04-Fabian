# from datetime import datetime, timezone
# from backend.app.modelos import db, ListaCompra, Usuario, Producto, ListaProducto
# import pytest

# def create_usuario(session, nombre='Test Usuario', contrasenha='password'):
#     """
#     Helper function to create a user with default or specified attributes.
#     """
#     new_usuario = Usuario(nombre=nombre, contrasenha=contrasenha)
#     session.add(new_usuario)
#     session.commit()
#     return new_usuario

# def create_producto(session, nombre='Test Producto', cantidad=10.00, unidad_medida='kg', comprado=False):
#     """
#     Helper function to create a product with default or specified attributes.
#     """
#     new_producto = Producto(nombre=nombre, cantidad=cantidad, unidad_medida=unidad_medida, comprado=comprado)
#     session.add(new_producto)
#     session.commit()
#     return new_producto

# def create_lista_compra(session, usuario_id, nombre='Lista de Compra Default', fecha_creacion=datetime.now(timezone.utc)):
#     """
#     Helper function to create a shopping list with default or specified attributes.
#     """
#     new_lista_compra = ListaCompra(usuario_id=usuario_id, nombre=nombre, fecha_creacion=fecha_creacion)
#     session.add(new_lista_compra)
#     session.commit()
#     return new_lista_compra

# def create_lista_producto(session, lista_compra_id, producto_id, cantidad=1.00):
#     """
#     Helper function to create a ListaProducto with default or specified attributes.
#     """
#     new_lista_producto = ListaProducto(lista_compra_id=lista_compra_id, producto_id=producto_id, cantidad=cantidad)
#     session.add(new_lista_producto)
#     session.commit()
#     return new_lista_producto

# @pytest.fixture
# def setup_lista_producto(session):
#     """
#     Fixture to setup necessary entities for ListaProducto tests.
#     """
#     usuario = create_usuario(session, nombre='Usuario ListaProducto', contrasenha='securepass123')
#     producto = create_producto(session, nombre='Producto para ListaProducto')
#     lista_compra = create_lista_compra(session, usuario.id, nombre='ListaCompra para ListaProducto')
#     return usuario, lista_compra, producto

# def test_create_lista_producto(app, session, setup_lista_producto):
#     with app.app_context():
#         _, lista_compra, producto = setup_lista_producto
#         create_lista_producto(session, lista_compra.id, producto.id, 5.00)

#         lista_producto = ListaProducto.query.filter_by(lista_compra_id=lista_compra.id, producto_id=producto.id).first()
#         assert lista_producto is not None
#         assert lista_producto.cantidad == 5.00

# def test_read_lista_producto(app, session, setup_lista_producto):
#     with app.app_context():
#         _, lista_compra, producto = setup_lista_producto
#         cantidad = 2.00
#         create_lista_producto(session, lista_compra.id, producto.id, cantidad)

#         lista_producto = ListaProducto.query.filter_by(lista_compra_id=lista_compra.id, producto_id=producto.id).first()
#         assert lista_producto is not None
#         assert lista_producto.cantidad == cantidad

# def test_update_lista_producto(app, session, setup_lista_producto):
#     with app.app_context():
#         _, lista_compra, producto = setup_lista_producto
#         lista_producto = create_lista_producto(session, lista_compra.id, producto.id, 3.00)

#         lista_producto.cantidad = 4.00
#         session.commit()

#         updated_lista_producto = ListaProducto.query.get(lista_producto.id)
#         assert updated_lista_producto is not None
#         assert updated_lista_producto.cantidad == 4.00

# def test_delete_lista_producto(app, session, setup_lista_producto):
#     with app.app_context():
#         _, lista_compra, producto = setup_lista_producto
#         lista_producto = create_lista_producto(session, lista_compra.id, producto.id, 1.00)

#         session.delete(lista_producto)
#         session.commit()

#         deleted_lista_producto = ListaProducto.query.get(lista_producto.id)
#         assert deleted_lista_producto is None
