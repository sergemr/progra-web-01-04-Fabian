# Historias de Usuario y Mapeo de Requisitos con Criterios de Aceptación

#### Registro de Usuarios (RF1, RF2)
1. **Como** usuario, **quiero** poder registrarme en la aplicación proporcionando mi nombre de usuario, correo electrónico y contraseña, **para** crear una cuenta personal.
   - **RF1**: Registro de usuario con información básica.
   - **RF2**: Validación de correo electrónico y criterios de seguridad para la contraseña.
   - **Criterios de Aceptación**:
     - La aplicación valida que el correo electrónico no esté ya en uso.
     - La contraseña debe cumplir con criterios mínimos de seguridad (ej., longitud, caracteres especiales).
     - El usuario recibe una confirmación de registro exitoso.

#### Inicio de Sesión (RF3, RF4)
2. **Como** usuario registrado, **quiero** poder iniciar sesión con mi correo electrónico y contraseña, **para** acceder a mis listas de compras y funcionalidades de la aplicación.
   - **RF3**: Inicio de sesión con credenciales.
   - **RF4**: Opción para recuperar contraseña olvidada.
   - **Criterios de Aceptación**:
     - El usuario puede iniciar sesión utilizando el correo electrónico y la contraseña.
     - Existe una opción visible para recuperar la contraseña.
     - En caso de datos incorrectos, se muestra un mensaje de error claro.

#### Operaciones CRUD de Productos (RF5, RF6)
3. **Como** usuario, **quiero** poder agregar, consultar, actualizar y eliminar productos en la base de datos, **para** gestionar eficientemente los productos disponibles para las listas de compras.
   - **RF5**: Agregar nuevos productos especificando detalles.
   - **RF6**: Consultar, actualizar y eliminar productos existentes.
   - **Criterios de Aceptación**:
     - Los usuarios pueden añadir productos indicando nombre, categoría, y precio.
     - Se pueden ver los detalles de cualquier producto y realizar actualizaciones o borrarlos.
     - Las operaciones de actualización y eliminación requieren confirmación del usuario.

#### Operaciones CRUD de Listas (RF7, RF8, RF9)
4. **Como** usuario, **quiero** poder crear, modificar y eliminar listas de compras, **para** organizar mis compras de manera eficiente.
   - **RF7**: Crear nuevas listas y nombrarlas.
   - **RF8**: Agregar, modificar y eliminar productos en las listas.
   - **RF9**: Eliminar listas completas.
   - **Criterios de Aceptación**:
     - Los usuarios pueden crear listas de compras y asignarles un nombre.
     - Dentro de una lista, se pueden agregar, modificar o eliminar productos.
     - Las listas de compras pueden ser eliminadas por completo, con una confirmación de seguridad.

#### Gestión de Listas (RF10, RF11, RF12, RF13, RF14)
5. **Como** usuario, **quiero** poder visualizar, modificar y gestionar mis listas de compras, **para** mantener un control sobre mis necesidades de compra y revisar el historial de compras completadas.
   - **RF10**: Visualizar todas las listas y productos.
   - **RF11**: Eliminar productos específicos de las listas.
   - **RF12**: Marcar productos como comprados.
   - **RF13**: Marcar listas de compras como completadas.
   - **RF14**: Visualizar listas completadas y revisar el historial de compras.
   - **Criterios de Aceptación**:
     - Los usuarios pueden ver todas sus listas y los productos en ellas.
     - Los productos pueden ser marcados como comprados y son visualmente distinguibles.
     - Las listas completas se pueden filtrar fuera de la vista principal y ser revisadas en una sección de historial.

### Requerimientos No Funcionales (RNF1 a RNF6)
6. **Como** usuario, **quiero** que la aplicación sea intuitiva y fácil de navegar, **para** mejorar mi experiencia de uso.
   - **RNF1**: Usabilidad.
   - **Criterios de Aceptación**:
     - Los usuarios pueden navegar por la aplicación sin instrucciones previas.
     - La aplicación proporciona una guía y feedback claro en todas las interacciones.

7. **Como** usuario, **quiero** que la aplicación sea accesible y funcione bien en cualquier dispositivo, **para** usarla en diferentes situaciones.
   - **RNF2**, **RNF6**: Accesibilidad y compatibilidad.
   - **Criterios de Aceptación**:
     - La aplicación es usable en los navegadores más populares y dispositivos móviles.
     - Cumple con los estándares de accesibilidad web (WCAG).

8. **Como** usuario, **quiero** que la aplicación responda rápidamente a mis acciones, **para** no perder tiempo esperando que cargue.
   - **RNF3**: Rendimiento.
   - **Criterios de Aceptación**:
     - Las acciones del usuario reciben respuesta en menos de 3 segundos.
     - La aplicación soporta hasta 100 usuarios simultáneos sin degradar el rendimiento.

9. **Como** usuario, **quiero** que mi información personal esté segura dentro de la aplicación, **para** usarla con confianza.
   - **RNF5**: Seguridad.
   - **Criterios de Aceptación**:
     - La aplicación utiliza HTTPS para todas sus transacciones.
     - Las contraseñas están hashadas y securizadas en la base de datos.