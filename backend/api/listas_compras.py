# # /home/localadmin/progra-web-01-04-Fabian/backend/api/listas_compras.py

# from flask import Blueprint, request, jsonify
# from backend.controllers.controller_listas_compras import ListasComprasController

# listas_compras_bp = Blueprint('listas_compras_bp', __name__)

# # Rutas
# listas_compras_bp.route('/listas-compras', methods=['POST'])(ListasComprasController.crear_lista_compras)
# listas_compras_bp.route('/listas-compras/<int:id_lista>/productos', methods=['POST'])(ListasComprasController.agregar_producto_a_lista)
# listas_compras_bp.route('/listas-compras/<int:id_lista>', methods=['GET'])(ListasComprasController.ver_lista_compras)
# listas_compras_bp.route('/usuarios/<int:id_usuario>/listas-compras', methods=['GET'])(ListasComprasController.listar_todas_listas_usuario)