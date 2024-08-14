from routes.marcaRouter import marcaRoutes
from routes.modeloController import modeloRoutes
from routes.produtoController import produtoRoutes
from routes.usuarioController import usuarioRoutes


def routeIndex(app):
    marcaRoutes(app)
    modeloRoutes(app)
    produtoRoutes(app)
    usuarioRoutes(app)
