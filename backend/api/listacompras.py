from flask import Blueprint
from backend.controladores.controlador_listacompras import ControladorListaCompras

listas_compras_bp = Blueprint('listas_compras_bp', __name__)

# Punto de API para crear nuevas listas de compras
listas_compras_bp.route('/v1/listascompras', methods=['POST'])(ControladorListaCompras.crear_lista_compras)
