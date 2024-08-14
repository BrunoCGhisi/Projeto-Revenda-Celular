from flask import request, render_template
from database.db import db
from models.produto import Produto

def produtoController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            produto = Produto(data['descricao'], data['idmarca'], data['idmodelo'], data['valor'], data['foto1'], data['fofo2'])
            db.session.add(produto)
            db.session.commit()
            return 'Produto adicionado com sucesso!', 200
        except Exception as e:
            return f'Não foi possível inserir. Erro {str(e)}', 405
        

    elif request.method == 'GET':
        try:
            data = Produto.query.all()
            print([ produto.to_dict() for produto in data])
            # newdata peggando os dados e deixando eles cute
            newData={'produto':[ produto.to_dict() for produto in data]}
            return newData, 200

        except Exception as e:
            return f'Não foi possível buscar. Erro {str(e)}', 405
        
        

    elif request.method == 'PUT':
            try:

                data = request.get_json() #pega todos os dados
                id = request.args.to_dict().get('id')
                prodtuo = Produto.query.get(id)

                if produto is None:
                    return{'error': 'Produto não encontrado'}, 405
                
                produto.descricao = data.get('descricao', produto.descricao)  
                produto.idmarca = data.get('idmarca', produto.idmarca)  
                produto.idmodelo = data.get('idmodelo', produto.idmodelo)
                produto.valor = data.get('valor', produto.valor)
                produto.foto1 = data.get('foto1', produto.foto1)
                produto.foto2 = data.get('foto2', produto.foto2)

                
                       

                
                db.session.commit()
                return "Produto atualizado com sucesso", 202

            except Exception as e:
                return f"Não foi possível atualizar o produto. Erro:{str(e)}", 405
            
    elif request.method == 'DELETE':
        print(request.args.to_dict().get('id'))
        try:
            data = request.args.to_dict().get('id')
            produto = Produto.query.get(data)

            if produto is None:
                return{'error': 'produto não encontrada'}, 405
            
            db.session.delete(produto)
            db.session.commit()
            return "marca deletada com sucesso", 202

        except Exception as e:
            return f"Não foi possível apagar a marca. Erro:{str(e)}", 405