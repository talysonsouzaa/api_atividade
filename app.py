from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

#USUARIOS = {
#     'Renan': '234'
#}
#
#@auth.verify_password
#def verificacao(login, senha):
#    print("Validando Usuario")
#    print(USUARIOS.get(login) == senha)
#   if not (login, senha):
#        return False
#   return USUARIOS.get(login) == senha

@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()
    

class Pessoa(Resource):
    @auth.login_required
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()

        if not pessoa:
            return {'mensagem': 'Pessoa não encontrada'}, 404

        response = {
            'nome': pessoa.nome,
            'idade': pessoa.idade,
            'id': pessoa.id
        }
        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
                    pessoa.idade = dados['idade']
        pessoa.save()
        response = {
                     'id': pessoa.id,
                     'nome': pessoa.nome,
                     'idade':pessoa.idade
                }
        return response
    
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = 'Pessoa {} excluida com sucesso!'.format(pessoa.nome)
        pessoa.delete()

        return {'Status':'Sucesso', 'Mensagem': mensagem}

class ListaPessoa(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        return response

    def post(self):
         dados = request.json
         pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
         pessoa.save()
         response = {
                    'id': pessoa.id,
                    'nome': pessoa.nome,
                    'idade': pessoa.idade

         }
         return response

class Listar_Atividades(Resource):
     def get(self):
          atividades = Atividades.query.all()
          response = [{'id':i.id, 'nome':i.nome, 'pessoa':i.pessoa.nome} for i in atividades]
          return response

     def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
                    'pessoa':atividade.pessoa.nome,
                    'nome' : atividade.nome,
                    'id' : atividade.id
          }
        return response
     
api.add_resource(Pessoa, '/pessoa/<string:nome>')
api.add_resource(ListaPessoa, '/pessoa/')
api.add_resource(Listar_Atividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)