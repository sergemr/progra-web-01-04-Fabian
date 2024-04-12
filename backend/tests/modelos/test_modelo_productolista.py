import pytest
from datetime import datetime, timezone
from backend.app.modelos import ProductoLista, Producto, ListaCompra, Usuario

def test_modelo_ProductoLista_tiene_todos_los_campos_correctos(session):
    """
    Prueba para asegurarse de que el modelo ProductoLista tiene todos los campos correctos
    """
    assert hasattr(ProductoLista, 'id')
    assert hasattr(ProductoLista, 'id_producto')
    assert hasattr(ProductoLista, 'id_lista')
    assert hasattr(ProductoLista, 'cantidad')
    assert hasattr(ProductoLista, 'comprado')
    assert hasattr(ProductoLista, 'creado_en')
    assert hasattr(ProductoLista, 'actualizado_en')

def test_creacion_ProductoLista(session):
    """
    Prueba la creación de una instancia de ProductoLista y valida la configuración de sus campos
    """
    usuario = Usuario(nombre_usuario="usuarioPrueba", hash_contrasena="contraseñaHash")
    producto = Producto(nombre="Pan", tipo_medida="Unidades")
    session.add(usuario)
    session.commit()

    lista_compra = ListaCompra(nombre="Compra semanal", id_usuario=usuario.id)
    session.add(producto)
    session.add(lista_compra)
    session.commit()

    producto_lista = ProductoLista(id_producto=producto.id, id_lista=lista_compra.id, cantidad=3, comprado=False)
    session.add(producto_lista)
    session.commit()

    assert producto_lista.cantidad == 3
    assert not producto_lista.comprado
    assert producto_lista.producto == producto
    assert producto_lista.lista_compra == lista_compra

def test_actualizacion_ProductoLista(session):
    """
    Prueba la actualización de una instancia de ProductoLista y valida la actualización de su estado 'comprado'
    """
    usuario = Usuario(nombre_usuario="usuarioPrueba2", hash_contrasena="contraseñaHash2")
    producto = Producto(nombre="Leche", tipo_medida="Litros")
    session.add(usuario)
    session.commit()

    lista_compra = ListaCompra(nombre="Compra mensual", id_usuario=usuario.id)
    session.add(producto)
    session.add(lista_compra)
    session.commit()

    producto_lista = ProductoLista(id_producto=producto.id, id_lista=lista_compra.id, cantidad=5, comprado=False)
    session.add(producto_lista)
    session.commit()
    
    producto_lista.comprado = True
    session.commit()

    assert producto_lista.comprado

def test_relacion_con_Producto_y_ListaCompra(session):
    """
    Prueba la relación entre ProductoLista con Producto y ListaCompra
    """
    usuario = Usuario(nombre_usuario="usuarioPrueba3", hash_contrasena="contraseñaHash3")
    producto = Producto(nombre="Arroz", tipo_medida="kg")
    session.add(usuario)
    session.add(producto)
    session.commit()

    lista_compra = ListaCompra(nombre="Compra diaria", id_usuario=usuario.id)
    session.add(lista_compra)
    session.commit()

    producto_lista = ProductoLista(id_producto=producto.id, id_lista=lista_compra.id, cantidad=2, comprado=False)
    session.add(producto_lista)
    session.commit()

    assert producto_lista.lista_compra == lista_compra
    assert producto_lista.producto == producto
    assert lista_compra.productos[0] == producto_lista
    assert producto.listas_productos[0] == producto_lista
