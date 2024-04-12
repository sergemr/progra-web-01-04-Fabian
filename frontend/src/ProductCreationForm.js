import React, { useState } from 'react';
// Import the centralized API instance instead of axios directly
import API from './api'; // Adjust the path as needed

function ProductCreationForm() {
    const [nombre, setNombre] = useState('');
    const [cantidad, setCantidad] = useState('');
    const [unidadMedida, setUnidadMedida] = useState('');
    const [imagen, setImagen] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setErrorMessage('');
        if (!nombre || !cantidad || !unidadMedida) {
            setErrorMessage('Nombre, cantidad y unidad de medida son obligatorios');
            return;
        }
        try {
            // Use API for the POST request
            await API.post('/productos', {
                nombre,
                cantidad,
                unidad_medida: unidadMedida,
                imagen, // Optional, can be empty
            });
            alert('Producto agregado con éxito!');
            // Optionally reset form fields
            setNombre('');
            setCantidad('');
            setUnidadMedida('');
            setImagen('');
        } catch (error) {
            setErrorMessage('Error al agregar el producto. Por favor, inténtelo de nuevo.');
        }
    };

    return (
        <div>
            <h2>Agregar Nuevo Producto</h2>
            {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Nombre del Producto:</label>
                    <input
                        type="text"
                        value={nombre}
                        onChange={(e) => setNombre(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Cantidad:</label>
                    <input
                        type="number"
                        value={cantidad}
                        onChange={(e) => setCantidad(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Unidad de Medida:</label>
                    <input
                        type="text"
                        value={unidadMedida}
                        onChange={(e) => setUnidadMedida(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Imagen (opcional):</label>
                    <input
                        type="text"
                        value={imagen}
                        onChange={(e) => setImagen(e.target.value)}
                    />
                </div>
                <button type="submit">Agregar Producto</button>
            </form>
        </div>
    );
}

export default ProductCreationForm;
