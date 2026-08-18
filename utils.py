from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Bruno', idade=61)
    print(pessoa) 
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Renan').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Alef').first()
    pessoa.nome = 'Davi'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Davi').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
   # altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()