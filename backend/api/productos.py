from flask import Blueprint
from backend.controladores.controlador_productos import ControladorProductos

# Definición del Blueprint para el módulo de productos
productos_bp = Blueprint('productos_bp', __name__)

# Punto de acceso de la API para agregar productos
productos_bp.route('/v1/productos', methods=['POST'])(ControladorProductos.agregar_producto)
