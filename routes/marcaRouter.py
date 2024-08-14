from controllers.marcaController import marcaController

def marcaRoutes(app):
    app.route('/marca', methods=['GET', 'POST', 'PUT', 'DELETE'])(marcaController)