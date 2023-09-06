from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


@app.route("/menu-category-items", methods=["GET"])
def get_menu_details():
    # Connect to the SQLite database
    connection = sqlite3.connect("starbucks_menu.db")
    cursor = connection.cursor()

    # Query the database to retrieve menu data
    cursor.execute("SELECT * FROM menu_item_details")
    menu_items = cursor.fetchall()

    # Close the database connection
    connection.close()

    # Convert the menu data to JSON and return it
    menu_json = [{"id": row[0],
                  "item_id": row[1],
                  "name": row[2],
                  "price": row[3],
                  "Description": row[4],
                  "subcategory": row[5]} for row in menu_items]
    return jsonify(menu_json)


@app.route("/menu-category", methods=["GET"])
def get_menu_category():
    # Connect to the SQLite database
    connection = sqlite3.connect("starbucks_menu.db")
    cursor = connection.cursor()

    # Query the database to retrieve menu data
    cursor.execute("SELECT * FROM menu_category_items")
    menu_items = cursor.fetchall()

    # Close the database connection
    connection.close()

    # Convert the menu data to JSON and return it
    menu_json = [{"id": row[0],
                  "category_id": row[1],
                  "subcategory": row[2]} for row in menu_items]
    return jsonify(menu_json)


@app.route("/menu", methods=["GET"])
def get_menu_items():
    # Connect to the SQLite database
    connection = sqlite3.connect("starbucks_menu.db")
    cursor = connection.cursor()

    # Query the database to retrieve menu data
    cursor.execute("SELECT * FROM categories")
    menu_items = cursor.fetchall()

    # Close the database connection
    connection.close()

    # Convert the menu data to JSON and return it
    menu_json = [{"name": row[1]} for row in menu_items]
    return jsonify(menu_json)


if __name__ == "__main__":
    app.run(debug=True)
