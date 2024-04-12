// frontend/src/ViewShoppingList.js
import React, { useState, useEffect } from 'react';
import API from './api'; // Ensure API is properly imported
import { useUser } from './UserContext';

function ViewShoppingList() {
  const { user } = useUser();
  const [shoppingLists, setShoppingLists] = useState([]);
  const [selectedListId, setSelectedListId] = useState('');
  const [listProducts, setListProducts] = useState([]);
  const [errorMessage, setErrorMessage] = useState('');

  useEffect(() => {
    if (user) {
      fetchShoppingLists();
    }
  }, [user]);

  const fetchShoppingLists = async () => {
    try {
      const response = await API.get(`/usuarios/${user.id}/listas-compras`);
      setShoppingLists(response.data);
    } catch (error) {
      setErrorMessage('Error al cargar las listas de compras.');
    }
  };

  const fetchListProducts = async (listId) => {
    try {
      const response = await API.get(`/listas-compras/${listId}`);
      setListProducts(response.data.productos);
    } catch (error) {
      setErrorMessage('Error al cargar los productos de la lista.');
    }
  };

  const handleListChange = (e) => {
    setSelectedListId(e.target.value);
    if (e.target.value) {
      fetchListProducts(e.target.value);
    }
  };

  return (
    <div>
      <h2>Ver Lista de Compras</h2>
      {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
      <select onChange={handleListChange} value={selectedListId}>
        <option value="">Selecciona una Lista</option>
        {shoppingLists.map(list => (
          <option key={list.lista_id} value={list.lista_id}>{list.nombre}</option>
        ))}
      </select>
      <ul>
        {listProducts.map(product => (
          <li key={product.producto_id}>{product.nombre} - {product.cantidad} {product.unidad_medida}</li>
        ))}
      </ul>
    </div>
  );
}

export default ViewShoppingList;
