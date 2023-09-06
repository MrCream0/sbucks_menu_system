import sqlite3

# Create or connect to the database
connection = sqlite3.connect('starbucks_menu.db')
cursor = connection.cursor()

# Create tables for menu categories, items, and item details
cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS menu_category_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER NOT NULL,
        subcategory TEXT,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS menu_item_details (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        price REAL,
        description TEXT,
        subcategory TEXT,
        FOREIGN KEY (item_id) REFERENCES menu_category_items(id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS menu_item_subcategories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        subcategory TEXT,
        FOREIGN KEY (item_id) REFERENCES menu_category_items(id)
    )
''')

# Insert main categories
main_categories = [
    ("Drinks",),
    ("Food",),
    ("At-Home Coffee",),
    ("Merchandise",)
]

cursor.executemany('''
    INSERT INTO categories (name)
    VALUES (?)
''', main_categories)

# Insert subcategories and menu items with prices and descriptions
menu_category_items = [
    # Drinks
    (1, "Oleato"),
    (1, "Hot Coffees"),
    (1, "Hot Teas"),
    (1, "Hot Drinks"),
    (1, "Frappuccino Blends"),
    (1, "Cold Coffees"),
    (1, "Iced Teas"),
    (1, "Cold Drinks"),
    # Food
    (2, "Hot Breakfast"),
    (2, "Oatmeal & Yogurt"),
    (2, "Bakery"),
    (2, "Snacks & Sweets"),
    # At-Home Coffee
    (3, "Whole Bean"),
    (3, "VIA Instant"),
    # Merchandise
    (4, "Cold Cups"),
    (4, "Tumblers"),
    (4, "Mugs"),
    (4, "Other"),
]

cursor.executemany('''
    INSERT INTO menu_category_items (category_id, subcategory)
    VALUES (?, ?)
''', menu_category_items)

# Define menu items for specific drink categories with prices and descriptions
menu_drink_oleato = [
    (1, "Oleato Golden Foam Cold Brew", 3.99, "enter desc", "oleato"),
    (1, "Oleato Caffe Latte with Oatmilk", 3.99, "enter desc", "oleato"),
    (1, "Oleato Iced Shaken Espresso with Oatmilk and Toffeenut", 3.99, "enter desc", "oleato"),
    (1, "Iced Chai Tea Latte with Oleato Golden Foam", 3.99, "enter desc", "oleato"),
    (1, "Iced Matcha Tea Latte with Oleato Golden Foam", 3.99, "enter desc", "oleato"),
    (1, "Paradise Drink Starbucks Refreshers Beverage with Oleato Golden Foam", 3.99, "enter desc", "oleato"),
    (1, "Dragon Drink Starbucks Refreshers with Oleato Golden Foam", 3.99, "enter desc", "oleato"),
]

menu_drink_hot_coffee_subcategory = [
    (1, "Americanos", "hot-coffee"),
    (2, "Brewed Coffees", "hot-coffee"),
    (3, "Cappuccinos", "hot-coffee"),
    (4, "Espresso Shots", "hot-coffee")
    # Add more items as needed
]

menu_drink_hotcoffee = [
    (1, "Caffe Americano", 1.99, "enter desc", "hot-coffee"),
    (2, "Featured Blonde Roast", 0.00, "enter desc", "hot-coffee"),
    (2, "Featured Medium Roast Pike Place Roast", 0.00, "enter desc", "hot-coffee"),
    (2, "Featured Dark Roast Sumatra", 0.00, "enter desc", "hot-coffee"),
    (2, "Featured Blonde Roast Veranda Blend", 0.00, "enter desc", "hot-coffee"),
    (2, "Featured Decaf Roast Decaf Pike Place Roast", 0.00, "enter desc", "hot-coffee"),
    (2, "Featured Medium Roast Pike Place Roast", 0.00, "enter desc", "hot-coffee"),
    (2, "Featured Dark Roast Caffe Verona", 0.00, "enter desc", "hot-coffee"),
    (2, "Featured Decaf Roast Decaf Pike Place Roast", 0.00, "enter desc", "hot-coffee"),
    (2, "Caffe Misto", 0.00, "enter desc", "hot-coffee"),
    (2, "Reserve", 0.00, "enter desc", "hot-coffee"),
    (2, "Reserve1", 0.00, "enter desc", "hot-coffee"),
    (2, "Reserve2", 0.00, "enter desc", "hot-coffee"),
    (3, "Cappuccino", 0.00, "enter desc", "hot-coffee"),
    # (4),
    # (4),
    # (5),
    # (5),
]


# Insert menu item details (prices and descriptions)
cursor.executemany('''
    INSERT INTO menu_item_details (item_id, name, price, description, subcategory)
    VALUES (?, ?, ?, ?, ?)
''', menu_drink_oleato)

cursor.executemany('''
    INSERT INTO menu_item_details (item_id, name, price, description, subcategory)
    VALUES (?, ?, ?, ?, ?)
''', menu_drink_hotcoffee)

cursor.executemany('''
    INSERT INTO menu_item_subcategories (item_id, name, subcategory)
    VALUES (?, ?, ?)
''', menu_drink_hot_coffee_subcategory)

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Starbucks menu database created and populated with your data.")
