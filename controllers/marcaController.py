from flask import request, render_template
from database.db import db
from models.marca import Marca

def marcaController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            marcas = Marca(data['nome'])
            db.session.add(marcas)
            db.session.commit()
            return 'Marca adicionado com sucesso!', 200
        except Exception as e:
            return f'Não foi possível inserir. Erro {str(e)}', 405
        

    elif request.method == 'GET':
        try:
            data = Marca.query.all()
            print([ marca.to_dict() for marca in data])
            # newdata peggando os dados e deixando eles cute
            newData={'marca':[ marca.to_dict() for marca in data]}
            return newData, 200

        except Exception as e:
            return f'Não foi possível buscar. Erro {str(e)}', 405
        
        

    elif request.method == 'PUT':
            try:
                id = request.args.to_dict().get('id')
                nome = Marca.query.get(id)
                data = request.get_json() #pega todos os dados

                if marca is None:
                    return{'error': 'Marca não encontrada'}, 405
                
                marca.nome = data.get('nome', marca.nome)
               
                db.session.commit()
                return "nome atualizado com sucesso", 202

            except Exception as e:
                return f"Não foi possível atualizar a Marca. Erro:{str(e)}", 405
            
    elif request.method == 'DELETE':
        print(request.args.to_dict().get('id'))
        try:
            data = request.args.to_dict().get('id')
            marca = Marca.query.get(data)

            if marca is None:
                return{'error': 'Marca não encontrada'}, 405
            
            db.session.delete(marca)
            db.session.commit()
            return "marca deletada com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar a marca. Erro:{str(e)}", 405