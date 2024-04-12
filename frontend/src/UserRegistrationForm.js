import React, { useState } from 'react';
// Import the centralized API instance instead of axios
import API from './api'; // Adjust the path as needed to correctly import the API instance

function UserRegistrationForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleRegister = async (e) => {
    e.preventDefault();
    setErrorMessage('');

    if (!username || !password) {
      setErrorMessage('Todos los campos son obligatorios');
      return;
    }

    try {
      // Use the API instance for the POST request
      await API.post('/usuarios', {
        nombre_usuario: username,
        contrasenha: password,
      });
      alert('Usuario registrado con éxito!');
      // Optionally reset form or redirect user
      setUsername('');
      setPassword('');
    } catch (error) {
      setErrorMessage('Error al registrar el usuario. Por favor, inténtelo de nuevo.');
    }
  };

  return (
    <div>
      <h2>Registro de Usuario</h2>
      {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
      <form onSubmit={handleRegister}>
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
        <button type="submit">Registrar</button>
      </form>
    </div>
  );
}

export default UserRegistrationForm;
