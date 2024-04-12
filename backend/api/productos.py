from flask import Blueprint
from backend.controladores.controlador_productos import ControladorProductos

# Definición del Blueprint para el módulo de productos
productos_bp = Blueprint('productos_bp', __name__)

# Punto de acceso de la API para agregar productos
productos_bp.route('/v1/productos', methods=['POST'])(ControladorProductos.agregar_producto)

# Puntos de acceso de la API para consultar productos
productos_bp.route('/v1/productos', methods=['GET'])(ControladorProductos.consultar_productos)
productos_bp.route('/v1/productos/<int:productoID>', methods=['GET'])(ControladorProductos.consultar_producto_por_id)

# Punto de acceso de la API para actualizar productos
productos_bp.route('/v1/productos/<int:productoID>', methods=['PUT'])(ControladorProductos.actualizar_producto)

# Punto de acceso de la API para eliminar productos
productos_bp.route('/v1/productos/<int:productoID>', methods=['DELETE'])(ControladorProductos.eliminar_producto)