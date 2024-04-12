# # Import necessary libraries and modules
# import pytest
# from backend.app.modelos import Producto

# # Helper function to add a product to the database for testing
# def add_product(session, nombre, cantidad, unidad_medida, imagen=None, comprado=False):
#     producto = Producto(nombre=nombre, cantidad=cantidad, unidad_medida=unidad_medida, imagen=imagen, comprado=comprado)
#     session.add(producto)
#     session.commit()

# class TestProductosController:
#     # Test case for successful product addition
#     def test_successful_product_addition(self, client, session):
#         product_data = {
#             'nombre': 'Producto Test',
#             'cantidad': 10,
#             'unidad_medida': 'kg',
#             'imagen': 'url_imagen',
#             'comprado': False
#         }
#         response = client.post('/api/productos', json=product_data)
#         assert response.status_code == 201
#         assert 'Producto agregado con éxito' in response.get_json()['mensaje']
#         assert 'producto_id' in response.get_json()

#     # Test case for adding a product with missing required fields
#     @pytest.mark.parametrize("product_data", [
#         {'cantidad': 10, 'unidad_medida': 'kg'},  # Missing name
#         {'nombre': 'Producto Test', 'unidad_medida': 'kg'},  # Missing quantity
#         {'nombre': 'Producto Test', 'cantidad': 10},  # Missing unit of measure
#     ])
#     def test_adding_product_with_missing_required_fields(self, client, product_data):
#         response = client.post('/api/productos', json=product_data)
#         assert response.status_code == 400
#         assert 'Faltan datos requeridos: nombre, cantidad, unidad_medida' in response.get_json()['error']

#     # Test case for database error during product addition
#     def test_database_error_during_product_addition(self, client, mocker):
#         product_data = {
#             'nombre': 'Producto Error',
#             'cantidad': 5,
#             'unidad_medida': 'litros',
#             'imagen': 'url_error',
#             'comprado': True
#         }
#         mocker.patch('backend.controllers.controller_productos.db.session.commit', side_effect=Exception('DB Error'))
#         response = client.post('/api/productos', json=product_data)
#         assert response.status_code == 500
#         assert 'Error al agregar producto: DB Error' in response.get_json()['error']

#     # Test case for successful retrieval of all products
#     def test_successful_retrieval_of_all_products(self, client, session):
#         # Add sample products to the database
#         add_product(session, 'Producto 1', 5, 'kg')
#         add_product(session, 'Producto 2', 2, 'litros')

#         response = client.get('/api/productos')
#         assert response.status_code == 200
#         products = response.get_json()
#         assert len(products) == 2
#         assert products[0]['nombre'] == 'Producto 1'
#         assert products[1]['nombre'] == 'Producto 2'

#     # Test case for database error during product retrieval
#     def test_database_error_during_product_retrieval(self, client, mocker):
#         mocker.patch('backend.app.modelos.Producto.query.all', side_effect=Exception('DB Retrieval Error'))
#         response = client.get('/api/productos')
#         assert response.status_code == 500
#         assert 'Error al recuperar los productos de la base de datos' in response.get_json()['error']
