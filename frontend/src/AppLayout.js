import React from 'react';
import { useUser } from './UserContext'; // Import useUser
import { Link, Route, Routes, useNavigate } from 'react-router-dom';
import UserRegistrationForm from './UserRegistrationForm';
import UserLoginForm from './UserLoginForm';
import ProductCreationForm from './ProductCreationForm';
import ShoppingListCreationForm from './ShoppingListCreationForm';
import ShoppingListManagement from './ShoppingListManagement';
import ViewShoppingList from './ViewShoppingList'; 

// frontend/src/AppLayout.js

function AppLayout() {
    const { user, logout: contextLogout } = useUser(); // Adjusted for clarity
    const navigate = useNavigate(); // Initialize useNavigate hook

    // Update logout function in AppLayout
    const logout = () => {
        const isConfirmed = window.confirm("¿Estás seguro de que quieres cerrar sesión?");
        if (isConfirmed) {
            contextLogout(); // This calls the logout method from UserContext
            navigate('/'); // Redirects to home page
        }
    };

    return (
        <div>
            <header style={{ backgroundColor: '#f0f0f0', padding: '10px', textAlign: 'center' }}>
                <h1>App Lista de Compras</h1>
            </header>
            <div style={{ display: 'flex', height: '90vh' }}>
                <aside style={{ flex: 1, backgroundColor: '#e0e0e0', padding: '20px' }}>
                    <nav>
                        <ul style={{ listStyleType: 'none', padding: 0 }}>
                            {!user && (
                                <>
                                    <li><Link to="/">Inicio de Sesión</Link></li>
                                    <li><Link to="/register">Registro de Usuarios</Link></li>
                                </>
                            )}
                            {user && (
                                <>
                                    <li><Link to="/add-product">Creación de Productos</Link></li>
                                    <li><Link to="/create-shopping-list">Creación de Listas de Compra</Link></li>
                                    <li><Link to="/shopping-list-management">Gestión de Listas de Compra</Link></li>
                                    <li><Link to="/view-shopping-list">Ver Listas de Compra</Link></li>
                                    <li><a href="#" onClick={logout}>Cerrar Sesión</a></li>
                                </>
                            )}
                        </ul>
                    </nav>
                </aside>
                <main style={{ flex: 4, padding: '20px' }}>
                    <Routes>
                        <Route path="/register" element={<UserRegistrationForm />} />
                        <Route path="/" element={<UserLoginForm />} />
                        <Route path="/add-product" element={<ProductCreationForm />} />
                        <Route path="/create-shopping-list" element={<ShoppingListCreationForm />} />
                        <Route path="/shopping-list-management" element={<ShoppingListManagement />} />
                        <Route path="/view-shopping-list" element={<ViewShoppingList />} />
                    </Routes>
                </main>
            </div>
        </div>
    );
}

export default AppLayout;
