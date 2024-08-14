from flask import request
from database.db import db
from models.usuario import Usuario

def usuarioController():
    if request.method == 'POST':
        try:

            data = request.get_json()
            usuario = Usuario(data['nome'], data['login'], data['senha'])
            db.session.add(usuario)
            db.session.commit()
            return 'Usuario add com sucesso', 200
        except Exception as e:
            return f'Ocorreu um erro, falha: {str(e)}', 400
            

    elif request.method == "GET":
        try:
            data = Usuario.query.all()
            newData = {'usuario': [usuario.to_dict() for usuario in data]}
            return newData, 200
        except Exception as e:
            return f'Ocorreu um erro, falha: {str(e)}', 405
        

    elif request.method == "PUT":
        try:

            id = request.args.to_dict().get('id')
            usuario = Usuario.query.get(id)
            data = request.get_json() #pega todos os dados

            if usuario is None:
                  return{'error': 'usuario não encontrado'}, 405
            
            usuario.nome = data.get('nome', usuario.nome)
            usuario.login = data.get('login', usuario.login)
            usuario.senha = data.get('senha', usuario.senha)            
            
            
            db.session.commit()
            return "usuario atualizado com sucesso", 202

        except Exception as e:
            return f'Ocorreu um erro, falha: {str(e)}', 405
    
    elif request.method == "DELETE":
        try:
            data = request.args.to_dict().get('id')
            usuario = Usuario.query.get(data)

            if usuario is None:
                return{'error': 'usuario não encontrado'}, 405
                
            db.session.delete(usuario)
            db.session.commit()
            return "usuario deletado com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar o usuario. Erro:{str(e)}", 405
            

        

