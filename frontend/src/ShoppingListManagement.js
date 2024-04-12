import React, { useState, useEffect } from 'react';
// Import the centralized API instance instead of axios directly
import API from './api'; // Adjust the path as needed
import { useUser } from './UserContext';

function ShoppingListManagement() {
    const { user } = useUser();
    const [shoppingLists, setShoppingLists] = useState([]);
    const [products, setProducts] = useState([]);
    const [selectedListId, setSelectedListId] = useState('');
    const [selectedProductId, setSelectedProductId] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    useEffect(() => {
        if (user) {
            fetchShoppingLists();
            fetchProducts();
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

    const fetchProducts = async () => {
        try {
            const response = await API.get('/productos');
            setProducts(response.data);
        } catch (error) {
            setErrorMessage('Error al cargar los productos.');
        }
    };

    const handleAddProductToList = async () => {
        if (!selectedListId || !selectedProductId) {
            setErrorMessage('Seleccione una lista y un producto.');
            return;
        }
        try {
            await API.post(`/listas-compras/${selectedListId}/productos`, {
                producto_id: selectedProductId,
                cantidad: 1, // This could be adjusted to allow specifying quantity
            });
            alert('Producto añadido con éxito.');
        } catch (error) {
            setErrorMessage('Error al añadir el producto a la lista.');
        }
    };

    return (
        <div>
            <h2>Gestión de Listas de Compra</h2>
            {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
            <div>
                <select onChange={e => setSelectedListId(e.target.value)} value={selectedListId}>
                    <option value="">Selecciona una Lista</option>
                    {shoppingLists.map(list => (
                        <option key={list.lista_id} value={list.lista_id}>{list.nombre}</option>
                    ))}
                </select>
                <select onChange={e => setSelectedProductId(e.target.value)} value={selectedProductId}>
                    <option value="">Selecciona un Producto</option>
                    {products.map(product => (
                        <option key={product.id} value={product.id}>{product.nombre}</option>
                    ))}
                </select>
                <button onClick={handleAddProductToList}>Añadir Producto a Lista</button>
            </div>
        </div>
    );
}

export default ShoppingListManagement;
