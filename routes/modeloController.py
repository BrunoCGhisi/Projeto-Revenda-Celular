from controllers.modeloController import modeloController

def modeloRoutes(app):
    app.route('/modelo', methods=['GET', 'POST', 'PUT', 'DELETE'])(modeloController)