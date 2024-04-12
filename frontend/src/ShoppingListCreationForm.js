import React, { useState } from 'react';
// Import the centralized API instance instead of axios directly
import API from './api'; // Adjust the path as needed
import { useUser } from './UserContext'; 

function ShoppingListCreationForm() {
    const [listName, setListName] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const { user } = useUser(); // Use the useUser hook to access the current user

    const handleCreateList = async (e) => {
        e.preventDefault();
        if (!listName) {
            setErrorMessage('El nombre de la lista es obligatorio');
            return;
        }
        try {
            // Make sure to check if user exists or is logged in
            if (!user || !user.id) {
                setErrorMessage('Usuario no identificado. Por favor, inicie sesión.');
                return;
            }
            // Use API for the POST request
            await API.post('/listas-compras', {
                nombre: listName,
                usuario_id: user.id, // Use the user ID from the context
            });
            alert('Lista de compras creada con éxito!');
            setListName('');
        } catch (error) {
            setErrorMessage('Error al crear la lista de compras. Por favor, inténtelo de nuevo.');
        }
    };

    return (
        <div>
            <h2>Crear Lista de Compras</h2>
            {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
            <form onSubmit={handleCreateList}>
                <div>
                    <label>Nombre de la Lista:</label>
                    <input
                        type="text"
                        value={listName}
                        onChange={(e) => setListName(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Crear Lista</button>
            </form>
        </div>
    );
}

export default ShoppingListCreationForm;
