import React, { useState } from 'react';
import API from './api'; // Import the centralized API instance instead of axios
import { useUser } from './UserContext';
import { useNavigate } from 'react-router-dom'; // Import useNavigate hook for redirection

function UserLoginForm() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const { setUser } = useUser(); // Use the setUser function from context
    const navigate = useNavigate(); // Initialize useNavigate hook

    const handleLogin = async (e) => {
        e.preventDefault();
        setErrorMessage('');
        if (!username || !password) {
            setErrorMessage('Todos los campos son obligatorios');
            return;
        }
        try {
            const response = await API.post('/usuarios/login', {
                nombre_usuario: username,
                contrasenha: password,
            });
            setUser(response.data.user); // Use setUser to update the global user state with the returned user object
            alert('Inicio de sesión exitoso!');
            navigate('/shopping-list-management'); // Adjust the path as needed
        } catch (error) {
            console.log(error.errorMessage);
            setErrorMessage('Error al iniciar sesión. Por favor, inténtelo de nuevo.');
        }
    };

    return (
        <div>
            <h2>Iniciar Sesión</h2>
            {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
            <form onSubmit={handleLogin}>
                <div>
                    <label>Nombre de Usuario:</label>
                    <input
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Contraseña:</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Iniciar Sesión</button>
            </form>
        </div>
    );
}

export default UserLoginForm;
