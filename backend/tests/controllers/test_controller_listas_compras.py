# import pytest
# from backend.app.modelos import Usuario, ListaCompra, Producto, ListaProducto
# from sqlalchemy.exc import IntegrityError

# # Helper function to add a user to the database for testing
# def add_user(session, nombre, contrasenha):
#     user = Usuario(nombre=nombre, contrasenha=contrasenha)
#     session.add(user)
#     session.commit()
#     return user

# # Helper function to add a product to the database for testing
# def add_product(session, nombre, cantidad, unidad_medida, imagen=None, comprado=False):
#     product = Producto(nombre=nombre, cantidad=cantidad, unidad_medida=unidad_medida, imagen=imagen, comprado=comprado)
#     session.add(product)
#     session.commit()
#     return product

# # Helper function to add a shopping list to the database for testing
# def add_shopping_list(session, nombre, usuario_id):
#     shopping_list = ListaCompra(nombre=nombre, usuario_id=usuario_id)
#     session.add(shopping_list)
#     session.commit()
#     return shopping_list

# # Helper function to add a product to a shopping list
# def add_product_to_shopping_list(session, lista_compra_id, producto_id, cantidad):
#     lista_producto = ListaProducto(
#         lista_compra_id=lista_compra_id,
#         producto_id=producto_id,
#         cantidad=cantidad
#     )
#     session.add(lista_producto)
#     session.commit()

# class TestListasComprasController:
#     def test_successful_creation_of_shopping_list(self, client, session):
#         user = add_user(session, 'testuser', 'testpass')
#         list_data = {
#             'nombre': 'Lista Test',
#             'usuario_id': user.id
#         }
#         response = client.post('/api/listas-compras', json=list_data)
#         assert response.status_code == 201
#         assert 'Lista de compras creada con éxito' in response.get_json()['mensaje']
#         assert 'lista_id' in response.get_json()

#     @pytest.mark.parametrize("list_data", [
#         {'usuario_id': 1},  # Missing nombre
#         {'nombre': 'Lista Test'},  # Missing usuario_id
#     ])
#     def test_creation_with_missing_required_fields(self, client, list_data):
#         response = client.post('/api/listas-compras', json=list_data)
#         assert response.status_code == 400
#         assert 'Nombre de la lista y ID del usuario son requeridos' in response.get_json()['error']

#     def test_user_not_found(self, client, session):
#         list_data = {
#             'nombre': 'Lista Test',
#             'usuario_id': 999  # Assuming this user does not exist
#         }
#         response = client.post('/api/listas-compras', json=list_data)
#         assert response.status_code == 404
#         assert 'Usuario no encontrado' in response.get_json()['error']

#     def test_database_error_during_creation(self, client, mocker, session):
#         user = add_user(session, 'testuser', 'testpass')
#         list_data = {
#             'nombre': 'Lista Error',
#             'usuario_id': user.id
#         }
#         mocker.patch('backend.controllers.controller_listas_compras.db.session.commit', side_effect=Exception('DB Error'))
#         response = client.post('/api/listas-compras', json=list_data)
#         assert response.status_code == 500
#         assert 'Error al crear la lista de compras: DB Error' in response.get_json()['error']

#     def test_successful_product_addition_to_shopping_list(self, client, session):
#         user = add_user(session, 'testuser', 'testpass')
#         product = add_product(session, 'Test Product', 1, 'kg')
#         shopping_list = add_shopping_list(session, 'Test List', user.id)
#         product_data = {
#             'producto_id': product.id,
#             'cantidad': 2  # Assume you want to add 2 kg of the product
#         }
#         response = client.post(f'/api/listas-compras/{shopping_list.id}/productos', json=product_data)
#         assert response.status_code == 201
#         assert 'Producto agregado a la lista de compras con éxito' in response.get_json()['mensaje']

#     @pytest.mark.parametrize("product_data", [
#         {'producto_id': 1},  # Missing cantidad
#         {'cantidad': 2},  # Missing producto_id
#     ])
#     def test_product_addition_with_missing_required_fields(self, client, product_data):
#         response = client.post('/api/listas-compras/1/productos', json=product_data)
#         assert response.status_code == 400
#         assert 'Producto ID y cantidad son requeridos' in response.get_json()['error']

#     def test_shopping_list_not_found_for_product_addition(self, client, session):
#         user = add_user(session, 'testuser', 'testpass')
#         product = add_product(session, 'Test Product', 1, 'kg')
#         product_data = {
#             'producto_id': product.id,
#             'cantidad': 2
#         }
#         # Assuming list ID 999 does not exist
#         response = client.post('/api/listas-compras/999/productos', json=product_data)
#         assert response.status_code == 404
#         assert 'Lista de compras no encontrada' in response.get_json()['error']

#     def test_product_not_found_during_addition_to_shopping_list(self, client, session):
#         user = add_user(session, 'testuser', 'testpass')
#         shopping_list = add_shopping_list(session, 'Test List', user.id)
#         product_data = {
#             'producto_id': 999,  # Assuming product ID 999 does not exist
#             'cantidad': 2
#         }
#         response = client.post(f'/api/listas-compras/{shopping_list.id}/productos', json=product_data)
#         assert response.status_code == 404
#         assert 'Producto no encontrado' in response.get_json()['error']

#     def test_database_error_during_product_addition(self, client, mocker, session):
#         user = add_user(session, 'testuser', 'testpass')
#         product = add_product(session, 'Test Product', 1, 'kg')
#         shopping_list = add_shopping_list(session, 'Test List', user.id)
#         product_data = {
#             'producto_id': product.id,
#             'cantidad': 2
#         }
#         mocker.patch('backend.controllers.controller_listas_compras.db.session.commit', side_effect=Exception('DB Error'))
#         response = client.post(f'/api/listas-compras/{shopping_list.id}/productos', json=product_data)
#         assert response.status_code == 500
#         assert 'Error al agregar producto a la lista de compras: DB Error' in response.get_json()['error']

#     def test_successful_retrieval_of_shopping_list(self, client, session):
#         user = add_user(session, 'testuser', 'testpass')
#         shopping_list = add_shopping_list(session, 'Test List', user.id)
#         product = add_product(session, 'Test Product', 1, 'kg')
#         add_product_to_shopping_list(session, shopping_list.id, product.id, 2)

#         response = client.get(f'/api/listas-compras/{shopping_list.id}')
#         assert response.status_code == 200
#         json_data = response.get_json()
#         assert json_data['nombre'] == 'Test List'
#         assert len(json_data['productos']) == 1
#         assert json_data['productos'][0]['nombre'] == 'Test Product'

#     def test_retrieval_of_nonexistent_shopping_list(self, client, session):
#         response = client.get('/api/listas-compras/999')  # Assuming list ID 999 does not exist
#         assert response.status_code == 404
#         assert 'Lista de compras no encontrada' in response.get_json()['error']

#     def test_successful_retrieval_of_all_lists_for_user(self, client, session):
#         # Setup: Add a user and some shopping lists for that user
#         user = add_user(session, 'existinguser', 'password123')
#         add_shopping_list(session, 'List 1', user.id)
#         add_shopping_list(session, 'List 2', user.id)

#         # Act: Retrieve all lists for the user
#         response = client.get(f'/api/usuarios/{user.id}/listas-compras')

#         # Assert: The response should have status code 200 and contain the lists
#         assert response.status_code == 200
#         data = response.get_json()
#         assert len(data) == 2  # Assuming the user has two lists
#         assert all('lista_id' in lista and 'nombre' in lista for lista in data)

#     def test_retrieval_for_nonexistent_user(self, client, session):
#         # Act: Attempt to retrieve lists for a user that does not exist
#         non_existent_user_id = 99999
#         response = client.get(f'/api/usuarios/{non_existent_user_id}/listas-compras')

#         # Assert: The response should have status code 404
#         assert response.status_code == 404
#         assert 'Usuario no encontrado' in response.get_json()['error']

#     def test_retrieval_for_user_with_no_lists(self, client, session):
#         # Setup: Add a user with no shopping lists
#         user = add_user(session, 'usernolists', 'password123')

#         # Act: Attempt to retrieve lists for the user
#         response = client.get(f'/api/usuarios/{user.id}/listas-compras')

#         # Assert: The response should have status code 200 and an empty list
#         assert response.status_code == 200
#         data = response.get_json()
#         assert data == []  # Expect an empty list if the user has no lists