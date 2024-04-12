# from backend.app.modelos import Producto

# def create_producto(session, nombre='Test Producto', cantidad=10.00, unidad_medida='kg', comprado=False):
#     """
#     Helper function to create a product with default or specified attributes.
#     """
#     new_producto = Producto(nombre=nombre, cantidad=cantidad, unidad_medida=unidad_medida, comprado=comprado)
#     session.add(new_producto)
#     session.commit()
#     return new_producto

# def test_create_producto(app, session):
#     with app.app_context():
#         create_producto(session, 'Test Producto', 10.00, 'kg', False)

#         producto = Producto.query.filter_by(nombre='Test Producto').first()
#         assert producto is not None
#         assert producto.nombre == 'Test Producto'
#         assert producto.cantidad == 10.00
#         assert producto.unidad_medida == 'kg'
#         assert producto.comprado == False

# def test_update_producto(app, session):
#     with app.app_context():
#         create_producto(session)  # Use default parameters to create a product.

#         producto = Producto.query.filter_by(nombre='Test Producto').first()
#         producto.nombre = 'Updated Producto'
#         session.commit()

#         updated_producto = Producto.query.filter_by(nombre='Updated Producto').first()
#         assert updated_producto is not None
#         assert updated_producto.nombre == 'Updated Producto'

# def test_delete_producto(app, session):
#     with app.app_context():
#         create_producto(session, 'Updated Producto')  # Create a product with the name to be deleted.

#         producto = Producto.query.filter_by(nombre='Updated Producto').first()
#         session.delete(producto)
#         session.commit()

#         deleted_producto = Producto.query.filter_by(nombre='Updated Producto').first()
#         assert deleted_producto is None

# Test if all expected fields (id, nombre, tipo_medida, creado_en, actualizado_en) and relationships (listas_productos) are present in the model.
def test_modelo_Producto_tiene_todos_los_campos_y_relaciones_correctos():
    from backend.app.modelos import Producto
    assert hasattr(Producto, 'id')
    assert hasattr(Producto, 'nombre')
    assert hasattr(Producto, 'tipo_medida')
    assert hasattr(Producto, 'creado_en')
    assert hasattr(Producto, 'actualizado_en')
    assert hasattr(Producto, 'listas_productos')