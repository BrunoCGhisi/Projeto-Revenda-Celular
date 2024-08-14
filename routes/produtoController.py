from controllers.produtoController import produtoController

def produtoRoutes(app):
    app.route('/produto', methods=['GET', 'POST', 'PUT', 'DELETE'])(produtoController)