from app import app
from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Leo', idade=23)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Renan').first()
    if pessoa:
        print(pessoa.idade)
    else:
        print('Renan não encontrado')

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Alef').first()
    if pessoa:
        pessoa.nome = 'Davi'
        pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Davi').first()
    if pessoa:
        pessoa.delete()

if __name__ == '__main__':
    with app.app_context():
        #insere_pessoas()
        # altera_pessoa()
        # exclui_pessoa()
        consulta_pessoas()