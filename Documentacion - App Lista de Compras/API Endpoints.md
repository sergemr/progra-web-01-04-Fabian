## Proceso de Autenticación

1. **Inicio de Sesión y Generación de Token JWT**
   - **Descripción**: Este endpoint permite a los usuarios iniciar sesión con su nombre de usuario y contraseña. Al autenticarse correctamente, se genera un token JWT.
   - **URL**: `/v1/login`
   - **Headers necesarios**:
     - `Content-Type: application/json`
   - **Body schema**:
     ```json
     {
       "nombreUsuario": "string",
       "contraseña": "string"
     }
     ```
   - **HTTP codes**:
     - `200 OK`: Inicio de sesión exitoso.
     - `401 Unauthorized`: Nombre de usuario o contraseña incorrectos.
   - **Ejemplo**:
     - **Request**:
       ```json
       {
         "nombreUsuario": "usuarioEjemplo",
         "contraseña": "Contraseña123!"
       }
       ```
     - **Response**:
       ```json
       {
         "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
       }
       ```

2. **Uso del Token y Almacenamiento Local**
   - Los tokens JWT deben almacenarse en el almacenamiento local del navegador o dispositivo móvil después del inicio de sesión.
   - Para cada solicitud a la API que requiera autenticación, se debe incluir el token en los headers como: 
     - `Authorization: Bearer <token>`

3. **Lista Permitida y Control de Revocación de Token**
   - Implementar una lista permitida en el servidor para gestionar tokens activos y su revocación.
   - En caso de necesidad de revocación, eliminar el token del almacenamiento local y solicitar al usuario volver a iniciar sesión.

4. **Refresco del Token**
   - Cuando el backend detecte un token próximo a expirar, enviará una notificación push al frontend solicitando al usuario si desea continuar usando la aplicación.
   - Si el usuario acepta, realizar una solicitud a `/v1/refresh_token` para obtener un nuevo token.

## 1. Registro de Usuarios

- **Descripción**: Permite a los nuevos usuarios crear una cuenta proporcionando su información básica.
- **URL Endpoint**: `/v1/registro`
- **Método**: `POST`
- **Headers necesarios**:
  - `Content-Type: application/json`
- **Body Schema**:
  ```json
  {
    "nombreUsuario": "string",
    "correoElectronico": "string",
    "contraseña": "string"
  }
  ```
- **HTTP Codes**:
  - `201 Created`: Usuario creado exitosamente.
  - `400 Bad Request`: Información proporcionada inválida o incompleta.
  - `409 Conflict`: El nombre de usuario o correo electrónico ya está en uso.
- **Ejemplo**:
  - **Request**:
    ```json
    {
      "nombreUsuario": "nuevoUsuario",
      "correoElectronico": "usuario@example.com",
      "contraseña": "ContraseñaSegura123"
    }
    ```
  - **Response** (201 Created):
    ```json
    {
      "mensaje": "Usuario creado exitosamente."
    }
    ```

## 2. Operaciones CRUD de Productos

### Agregar Nuevo Producto

- **Descripción**: Permite a los usuarios agregar nuevos productos a la base de datos.
- **URL Endpoint**: `/v1/productos`
- **Método**: `POST`
- **Headers necesarios**:
  - `Content-Type: application/json`
  - `Authorization: Bearer <token>`
- **Body Schema**:
  ```json
  {
    "nombre": "string",
    "categoria": "string",
    "precio": "number"
  }
  ```
- **HTTP Codes**:
  - `201 Created`: Producto agregado exitosamente.
  - `400 Bad Request`: Información proporcionada inválida o incompleta.
  - `401 Unauthorized`: No autenticado o token inválido.
- **Ejemplo**:
  - **Request**:
    ```json
    {
      "nombre": "Manzanas",
      "categoria": "Alimentos",
      "precio": 0.99
    }
    ```
  - **Response** (201 Created):
    ```json
    {
      "mensaje": "Producto agregado exitosamente."
    }
    ```
Continuaremos definiendo los endpoints para las operaciones CRUD de productos restantes: consultar, actualizar y eliminar productos.

### Consultar Productos

- **Descripción**: Permite a los usuarios consultar todos los productos disponibles o un producto específico por su ID.
- **URL Endpoint**: Para todos los productos: `/v1/productos`
  Para un producto específico: `/v1/productos/{productoID}`
- **Método**: `GET`
- **Headers necesarios**:
  - `Authorization: Bearer <token>`
- **HTTP Codes**:
  - `200 OK`: Consulta exitosa.
  - `401 Unauthorized`: No autenticado o token inválido.
  - `404 Not Found`: Producto no encontrado (en caso de buscar por ID).
- **Ejemplo**:
  - **Request** (Todos los productos):
    - No requiere body.
  - **Response** (200 OK):
    ```json
    [
      {
        "productoID": 1,
        "nombre": "Manzanas",
        "categoria": "Alimentos",
        "precio": 0.99
      },
      {
        "productoID": 2,
        "nombre": "Monitor 24 pulgadas",
        "categoria": "Electrónicos",
        "precio": 199.99
      }
    ]
    ```

### Actualizar Producto

- **Descripción**: Permite a los usuarios actualizar los detalles de un producto existente.
- **URL Endpoint**: `/v1/productos/{productoID}`
- **Método**: `PUT`
- **Headers necesarios**:
  - `Content-Type: application/json`
  - `Authorization: Bearer <token>`
- **Body Schema**:
  ```json
  {
    "nombre": "string",
    "categoria": "string",
    "precio": "number"
  }
  ```
- **HTTP Codes**:
  - `200 OK`: Producto actualizado exitosamente.
  - `400 Bad Request`: Información proporcionada inválida o incompleta.
  - `401 Unauthorized`: No autenticado o token inválido.
  - `404 Not Found`: Producto no encontrado.
- **Ejemplo**:
  - **Request**:
    ```json
    {
      "nombre": "Manzanas Gala",
      "categoria": "Alimentos",
      "precio": 1.09
    }
    ```
  - **Response** (200 OK):
    ```json
    {
      "mensaje": "Producto actualizado exitosamente."
    }
    ```

### Eliminar Producto

- **Descripción**: Permite a los usuarios eliminar un producto existente.
- **URL Endpoint**: `/v1/productos/{productoID}`
- **Método**: `DELETE`
- **Headers necesarios**:
  - `Authorization: Bearer <token>`
- **HTTP Codes**:
  - `200 OK`: Producto eliminado exitosamente.
  - `401 Unauthorized`: No autenticado o token inválido.
  - `404 Not Found`: Producto no encontrado.
- **Ejemplo**:
  - **Request**: No requiere body.
  - **Response** (200 OK):
    ```json
    {
      "mensaje": "Producto eliminado exitosamente."
    }
    ```

### Crear Nueva Lista de Compras

- **Descripción**: Permite a los usuarios crear una nueva lista de compras asignándole un nombre.
- **URL Endpoint**: `/v1/listas`
- **Método**: `POST`
- **Headers necesarios**:
  - `Content-Type: application/json`
  - `Authorization: Bearer <token>`
- **Body Schema**:
  ```json
  {
    "nombre": "string"
  }
  ```
- **HTTP Codes**:
  - `201 Created`: Lista de compras creada exitosamente.
  - `400 Bad Request`: Información proporcionada inválida o incompleta.
  - `401 Unauthorized`: No autenticado o token inválido.
- **Ejemplo**:
  - **Request**:
    ```json
    {
      "nombre": "Compras Semanales"
    }
    ```
  - **Response** (201 Created):
    ```json
    {
      "mensaje": "Lista de compras creada exitosamente."
    }
    ```

## 3. Agregar Producto a una Lista

- **Descripción**: Permite a los usuarios agregar un producto a una lista de compras especificando la cantidad.
- **URL Endpoint**: `/v1/listas/{listaID}/productos`
- **Método**: `POST`
- **Headers necesarios**:
  - `Content-Type: application/json`
  - `Authorization: Bearer <token>`
- **Body Schema**:
  ```json
  {
    "productoID": "int",
    "cantidad": "int"
  }
  ```
- **HTTP Codes**:
  - `201 Created`: Producto agregado a la lista exitosamente.
  - `400 Bad Request`: Información proporcionada inválida o incompleta.
  - `401 Unauthorized`: No autenticado o token inválido.
  - `404 Not Found`: Lista de compras no encontrada.
- **Ejemplo**:
  - **Request**:
    ```json
    {
      "productoID": 1,
      "cantidad": 3
    }
    ```
  - **Response** (201 Created):
    ```json
    {
      "mensaje": "Producto agregado a la lista exitosamente."
    }
    ```

### Consultar Listas de Compras y Sus Productos

- **Descripción**: Permite a los usuarios ver todas sus listas de compras y los productos agregados a cada una.
- **URL Endpoint**: `/v1/listas`
- **Método**: `GET`
- **Headers necesarios**:
  - `Authorization: Bearer <token>`
- **HTTP Codes**:
  - `200 OK`: Consulta exitosa.
  - `401 Unauthorized`: No autenticado o token inválido.
- **Ejemplo**:
  - **Request**: No requiere body.
  - **Response** (200 OK):
    ```json
    [
      {
        "listaID": 1,
        "nombre": "Compras Semanales",
        "productos": [
          {
            "productoID": 1,
            "nombre": "Manzanas",
            "cantidad": 3,
            "comprado": false
          }
        ]
      }
    ]
    ```

### Eliminar Producto de una Lista de Compras

- **Descripción**: Permite a los usuarios eliminar un producto específico de una lista de compras.
- **URL Endpoint**: `/v1/listas/{listaID}/productos/{productoID}`
- **Método**: `DELETE`
- **Headers necesarios**:
  - `Authorization: Bearer <token>`
- **HTTP Codes**:
  - `200 OK`: Producto eliminado de la lista exitosamente.
  - `401 Unauthorized`: No autenticado o token inválido.
  - `404 Not Found`: Lista de compras o producto no encontrado en la lista.
- **Ejemplo**:
  - **Request**: No requiere body.
  - **Response** (200 OK):
    ```json
    {
      "mensaje": "Producto eliminado de la lista exitosamente."
    }
    ```

### Eliminar Lista de Compras Completa

- **Descripción**: Permite a los usuarios eliminar una lista de compras completa, incluyendo todos los productos asociados a ella.
- **URL Endpoint**: `/v1/listas/{listaID}`
- **Método**: `DELETE`
- **Headers necesarios**:
  - `Authorization: Bearer <token>`
- **HTTP Codes**:
  - `200 OK`: Lista de compras eliminada exitosamente.
  - `401 Unauthorized`: No autenticado o token inválido.
  - `404 Not Found`: Lista de compras no encontrada.
- **Ejemplo**:
  - **Request**: No requiere body.
  - **Response** (200 OK):
    ```json
    {
      "mensaje": "Lista de compras eliminada exitosamente."
    }
    ```

### Marcar Producto como Comprado

- **Descripción**: Permite a los usuarios marcar un producto específico en una lista como comprado.
- **URL Endpoint**: `/v1/listas/{listaID}/productos/{productoID}/comprar`
- **Método**: `POST`
- **Headers necesarios**:
  - `Authorization: Bearer <token>`
- **Body Schema**: No requiere un cuerpo específico, ya que el acto de enviar la solicitud a este endpoint implica la acción de marcar el producto como comprado.
- **HTTP Codes**:
  - `200 OK`: Producto marcado como comprado exitosamente.
  - `401 Unauthorized`: No autenticado o token inválido.
  - `404 Not Found`: Lista de compras o producto no encontrado en la lista.
- **Ejemplo**:
  - **Request**: No requiere body.
  - **Response** (200 OK):
    ```json
    {
      "mensaje": "Producto marcado como comprado exitosamente."
    }
    ```

### Marcar Lista de Compras como Completada

- **Descripción**: Permite a los usuarios marcar una lista de compras completa como "Completada".
- **URL Endpoint**: `/v1/listas/{listaID}/completar`
- **Método**: `POST`
- **Headers necesarios**:
  - `Authorization: Bearer <token>`
- **Body Schema**: No requiere un cuerpo, el acto de enviar la solicitud a este endpoint implica la acción de marcar la lista como completada.
- **HTTP Codes**:
  - `200 OK`: Lista de compras marcada como completada exitosamente.
  - `401 Unauthorized`: No autenticado o token inválido.
  - `404 Not Found`: Lista de compras no encontrada.
- **Ejemplo**:
  - **Request**: No requiere body.
  - **Response** (200 OK):
    ```json
    {
      "mensaje": "Lista de compras marcada como completada exitosamente."
    }
    ```