from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def load_books():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    books = load_books()
    total = len(books)
    sold = len([b for b in books if b['sold']])
    available = total - sold
    return render_template('index.html', books=books, total=total, sold=sold, available=available)

@app.route('/katalog')
def katalog():
    books = load_books()
    return render_template('katalog.html', books=books)

@app.route('/buyurtma')
def buyurtma():
    return render_template('buyurtma.html')

@app.route('/biz-haqimizda')
def biz_haqimizda():
    return render_template('biz-haqimizda.html')

@app.route('/api/books')
def api_books():
    books = load_books()
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
