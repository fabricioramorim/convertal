from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'The Lord of the Rings',
        'author': 'J. R. R. Tolkien',
    },
    {
        'id': 2,
        'title': 'Harry Potter',
        'author': 'J. K. Rowling',
    },
    {
        'id': 3,
        'title': 'The Hobbit',
        'author': 'J. R. R. Tolkien',
    },
]

#consultar todos
@app.route('/books', methods=['GET'])
def get_book():
    return jsonify({'books': books})

#consultar por id
@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        return jsonify({'message': 'Book not found'})
    return jsonify({'book': book[0]})

#editar livro por id
@app.route('/books/<int:id>', methods=['PUT'])
def edit_book_by_id(id):
    book_edited = request.get_json()
    for index, book in enumerate(books):
        if book['id'] == id:
            books[index].update(book_edited)
            return jsonify({book['id']: book_edited})

#criar novo livro
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify({'books': books})

#deletar livro por id
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book_by_id(id):
    for index, book in enumerate(books):
        if book['id'] == id:
            del books[index]
            return jsonify({'message': 'Book deleted'})
    return jsonify({'message': 'Book not found'})

app.run(port=5000, host='localhost', debug=True)