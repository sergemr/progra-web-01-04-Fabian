import pytest
import time
from datetime import datetime, timezone
from backend.app.modelos import Producto
from sqlalchemy import func

def test_campos_modelo_producto(session):
    """
    Prueba para asegurar que el modelo Producto tiene todos los campos correctos
    """
    assert hasattr(Producto, 'id')
    assert hasattr(Producto, 'nombre')
    assert hasattr(Producto, 'tipo_medida')
    assert hasattr(Producto, 'creado_en')
    assert hasattr(Producto, 'actualizado_en')
    assert hasattr(Producto, 'listas_productos')

def test_creacion_producto(session):
    """
    Prueba la creación de un Producto y valida la configuración automática de los campos `creado_en` y `actualizado_en`
    """
    producto = Producto(nombre='Arroz', tipo_medida='kg')
    session.add(producto)
    session.commit()
    assert producto.creado_en != None
    assert producto.actualizado_en != None

def test_actualizacion_producto(session):
    """
    Prueba la actualización de un Producto y valida que el campo `actualizado_en` cambie en consecuencia
    """
    producto = Producto(nombre='Arroz', tipo_medida='kg')
    session.add(producto)
    session.commit()
    fecha_actualizacion_creacion = producto.actualizado_en
    time.sleep(1)
    producto.nombre = 'Arroz Integral'
    session.commit()
    assert producto.actualizado_en != fecha_actualizacion_creacion
    assert producto.actualizado_en > fecha_actualizacion_creacion

def test_nombre_no_nulo(session):
    """
    Prueba para asegurar que no se puede crear un Producto sin un `nombre`
    """
    with pytest.raises(Exception):
        producto = Producto(tipo_medida='Unidades')
        session.add(producto)
        session.commit()

def test_tipo_medida_no_nulo(session):
    """
    Prueba para asegurar que no se puede crear un Producto sin un `tipo_medida`
    """
    with pytest.raises(Exception):
        producto = Producto(nombre='Pan')
        session.add(producto)
        session.commit()
