from controllers.usuarioController import usuarioController

def usuarioRoutes(app):
    app.route('/usuario', methods=['GET', 'POST', 'PUT', 'DELETE'])(usuarioController)