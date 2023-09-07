from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect('starbucks_menu.db')
    connection.row_factory = sqlite3.Row
    return connection


def execute_query(query, args=()):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    conn.close()


@app.route('/categories', methods=['GET'])
def get_categories():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    conn.close()
    return jsonify([dict(category) for category in categories])


@app.route('/menu-items', methods=['GET'])
def get_menu_items():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM menu_item_details')
    menu_items = cursor.fetchall()
    conn.close()
    return jsonify([dict(item) for item in menu_items])


@app.route('/menu-items/<int:item_id>', methods=['GET'])
def get_menu_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM menu_item_details WHERE id = ?', (item_id,))
    menu_item = cursor.fetchone()
    conn.close()
    if menu_item:
        return jsonify(dict(menu_item))
    else:
        return jsonify({"message": "Menu item not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
