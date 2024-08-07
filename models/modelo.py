from database.db import db

class Modelo(db.Model):
    def to_dict(self):
        return{
            'id': self.codigo,
            'nome': self.nome  
        }
    
    id = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    nome = db.Column(db.String(45), nullable=False)

    def __init__(self, nome):
        self.nome = nome