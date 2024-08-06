from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {'id': 1, 'título': '1984', 'autor': 'George Orwell'},
    {'id': 2, 'título': 'O Senhor dos Anéis', 'autor': 'J. R. R. Tolkien'},
    {'id': 3, 'título': 'O Prisioneiro de Azkhaban', 'autor': 'J. K. Rowling'},
]

@app.route('/api/livros', methods=['GET'])
def get_livros():
    return jsonify(livros)

@app.route('/api/livros/<int:id>', methods=['GET'])
def get_livro(id):
    livro = next(
        (livro for livro in livros if livro['id'] == id),
        None
    )
    return jsonify(livro) if livro else ('', 404)

@app.route('/api/livros', methods=['POST'])
def add_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

if __name__ == '__main__':
    app.run(port=5000, debug=True)