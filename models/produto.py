from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Produto(db.Model):
    def to_dict(self):
        return{
            'id': self.codigo,
            'descricao': self.descricao,  
            'idmarca': self.codmarca,
            'idmodelo': self.codmodelo,  
            'valor': self.valor,  
            'foto1': self.foto1,  
            'foto2': self.foto2  
        }
    
    id = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    descricao = db.Column(db.String(45), nullable=False)
    idmarca = db.Column(ForeignKey('marca.idmarca'), nullable=False)
    idmodelo = db.Column(ForeignKey('modelo.idmodelo'), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    foto1 = db.Column(db.Text, nullable=False)
    foto2 = db.Column(db.Text, nullable=False)

    modelo = relationship('Modelo', backref='produto')
    marca = relationship('Marca', backref='produto')

    def __init__(self, nome, descricao, idmarca, idmodelo, valor, foto1, foto2):
        self.nome = nome
        self.descricao = descricao
        self.idmarca = idmarca
        self.idmodelo = idmodelo
        self.valor = valor
        self.foto1 = foto1
        self.foto2 = foto2

    
