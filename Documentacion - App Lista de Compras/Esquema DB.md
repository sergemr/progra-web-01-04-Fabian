#### Usuarios
- **Descripción de la Entidad:** Almacena información sobre los usuarios que se registran y utilizan la aplicación.
  - `UsuarioID (INT, Clave Primaria)`: Identificador único para cada usuario.
  - `NombreUsuario (VARCHAR(50))`: Nombre elegido por el usuario. Es único.
  - `CorreoElectronico (VARCHAR(100))`: Dirección de correo electrónico del usuario. Se utiliza para iniciar sesión y comunicarse.
  - `HashContraseña (VARCHAR(255))`: Versión hasheada de la contraseña del usuario para su almacenamiento seguro.
  - `CreatedAt (DATETIME)`: Marca de tiempo cuando se creó el registro del usuario.
  - `UpdatedAt (DATETIME)`: Marca de tiempo cuando se actualizó el registro del usuario por última vez.

### Tabla Productos
- **Descripción de la Entidad:** Contiene detalles sobre los productos que pueden ser añadidos a las listas de compras.
  - `ProductoID (INT, Clave Primaria)`: Identificador único para cada producto.
  - `Nombre (VARCHAR(100))`: Nombre del producto.
  - `TipoMedida (VARCHAR(50))`: Tipo de medida del producto (p.ej., unidad, kg, litro, etc.).
  - `CreatedAt (DATETIME)`: Marca de tiempo cuando se creó el registro del producto.
  - `UpdatedAt (DATETIME)`: Marca de tiempo cuando se actualizó el registro del producto por última vez.

#### ListasDeCompras
- **Descripción de la Entidad:** Representa listas de compras individuales creadas por los usuarios.
  - `ListaID (INT, Clave Primaria)`: Identificador único para cada lista.
  - `UsuarioID (INT, Clave Extranjera)`: ID del usuario propietario de la lista.
  - `Nombre (VARCHAR(100))`: Nombre de la lista de compras.
  - `Estado (VARCHAR(20))`: Indica el estado de la lista (p.ej., Pendiente, Completada).
  - `CreatedAt (DATETIME)`: Marca de tiempo cuando se creó la lista.
  - `UpdatedAt (DATETIME)`: Marca de tiempo cuando se actualizó la lista por última vez.

#### ProductoLista
- **Descripción de la Entidad:** Tabla de unión para la relación muchos a muchos entre Productos y ListasDeCompras, con información adicional.
  - `ProductoListaID (INT, Clave Primaria)`: Identificador único para cada entrada.
  - `ProductoID (INT, Clave Extranjera)`: ID del producto en la lista.
  - `ListaID (INT, Clave Extranjera)`: ID de la lista que contiene el producto.
  - `Cantidad (INT)`: Cantidad del producto en la lista.
  - `Comprado (BOOLEAN)`: Si el producto ha sido comprado (Verdadero o Falso).
  - `CreatedAt (DATETIME)`: Marca de tiempo cuando se creó la entrada en ProductoLista.
  - `UpdatedAt (DATETIME)`: Marca de tiempo cuando se actualizó la entrada en ProductoLista por última vez.