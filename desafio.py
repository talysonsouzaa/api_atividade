from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
db = SQLAlchemy(app)


class Programador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    email = db.Column(db.String(100))



class Habilidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))


class ProgramadorHabilidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    programador = db.Column(db.Integer, db.ForeignKey('programador.id'))
    habilidade = db.Column(db.Integer, db.ForeignKey('habilidade.id'))


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)