from .database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.String(100), nullable=False)
    dataNascimento = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f'<User {self.nome}>'