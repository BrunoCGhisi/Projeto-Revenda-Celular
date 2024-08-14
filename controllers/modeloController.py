from flask import request, render_template
from database.db import db
from models.modelo import Modelo

def modeloController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            modelo = Modelo(data['nome'])
            db.session.add(modelo)
            db.session.commit()
            return 'modelo adicionado com sucesso!', 200
        except Exception as e:
            return f'Não foi possível inserir. Erro {str(e)}', 405
        

    elif request.method == 'GET':
        try:
            data = Modelo.query.all()
            print([ modelo.to_dict() for modelo in data])
            # newdata peggando os dados e deixando eles cute
            newData={'modelo':[ modelo.to_dict() for modelo in data]}
            return newData, 200

        except Exception as e:
            return f'Não foi possível buscar. Erro {str(e)}', 405
        
        

    elif request.method == 'PUT':
            try:
                id = request.args.to_dict().get('id')
                nome = Modelo.query.get(id)
                data = request.get_json() #pega todos os dados

                if modelo is None:
                    return{'error': 'modelo não encontrada'}, 405
                
                modelo.nome = data.get('nome', modelo.nome)
               
                db.session.commit()
                return "nome atualizado com sucesso", 202

            except Exception as e:
                return f"Não foi possível atualizar a modelo. Erro:{str(e)}", 405
            
    elif request.method == 'DELETE':
        print(request.args.to_dict().get('id'))
        try:
            data = request.args.to_dict().get('id')
            modelo = Modelo.query.get(data)

            if modelo is None:
                return{'error': 'modelo não encontrada'}, 405
            
            db.session.delete(modelo)
            db.session.commit()
            return "modelo deletada com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar a modelo. Erro:{str(e)}", 405