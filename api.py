from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.db'

db = SQLAlchemy(app)

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

livros = [
    {'id': 1, 'titulo': '1984', 'autor': 'George Orwell'},
    {'id': 2, 'titulo': 'O Senhor dos Anéis', 'autor': 'J. R. R. Tolkien'},
    {'id': 3, 'titulo': 'O Prisioneiro de Azkhaban', 'autor': 'J. K. Rowling'},
]

@app.route('/api/livros', methods=['GET'])
def get_livros():
    livros = Livro.query.all()
    return jsonify([{
        "id":livro.id, 
        "titulo":livro.titulo,
        "autor":livro.autor
    } for livro in livros])

@app.route('/api/livros/<int:id>', methods=['GET'])
def get_livro(id):
    livro = Livro.query.get(id)
    
    return jsonify({
        "id":livro.id, 
        "titulo":livro.titulo,
        "autor":livro.autor
    }) if livro else ('', 404)

@app.route('/api/livros', methods=['POST'])
def add_livro():
    dados = request.get_json()
    novo_livro = Livro(
        titulo=dados['titulo'], 
        autor=dados['autor'])
    db.session.add(novo_livro)
    db.session.commit()
    return jsonify({
        "id":novo_livro.id, 
        "titulo":novo_livro.titulo,
        "autor":novo_livro.autor
    }), 201

if __name__ == '__main__':
    app.run(port=5000, debug=True)