from database.db import db


class Usuario(db.Model):
    def to_dict(self):
        return {
            'id':   self.codigo,
            'nome': self.nome, 
            'login':self.login, 
            'senha':self.senha 
        }
    id = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    login = db.Column(db.String(45), nullable=False)
    senha = db.Column(db.String(45), nullable=False)

    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.login = senha