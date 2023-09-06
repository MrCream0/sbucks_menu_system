import sqlite3

connection = sqlite3.connect('starbucks_menu.db')
cursor = connection.cursor()

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
    (4, "Espresso Shots", "hot-coffee"),
    (5, "Flat Whites", "hot-coffee"),
    (6, "Lattes", "hot-coffee"),
    (7, "Macchiatos", "hot-coffee"),
    (8, "Mochas", "hot-coffee"),
    (9, "Travelers", "hot-coffee"),
]

menu_drink_hot_coffee = [
    (1, "Caffe Americano", 0.00, "enter desc", "hot-coffee"),
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
    (4, "Espresso", 0.00, "enter desc", "hot-coffee"),
    (4, "Espresso Con Panna", 0.00, "enter desc", "hot-coffee"),
    (5, "Flat White", 0.00, "enter desc", "hot-coffee"),
    (5, "Honey Almondmilk Flat White", 0.00, "enter desc", "hot-coffee"),
    (6, "Pumpkin Spice Latte", 0.00, "enter desc", "hot-coffee"),
    (6, "Oleato Caffe Latte with Oatmilk", 0.00, "enter desc", "hot-coffee"),
    (6, "Caffe Latte", 0.00, "enter desc", "hot-coffee"),
    (6, "Connamon Dolce Latte", 0.00, "enter desc", "hot-coffee"),
    (6, "Starbucks Reserve Latte", 0.00, "enter desc", "hot-coffee"),
    (6, "Starbucks Reserve Hazelnut Bianco Latte", 0.00, "enter desc", "hot-coffee"),
    (6, "Starbucks Blonde Vanilla Latte", 0.00, "enter desc", "hot-coffee"),
    (7, "Apple Crisp Oatmilk Macchiato", 0.00, "enter desc", "hot-coffee"),
    (7, "Caramel Macchiato", 0.00, "enter desc", "hot-coffee"),
    (7, "Espresso Macchiato", 0.00, "enter desc", "hot-coffee"),
    (8, "Caffe Mocha", 0.00, "enter desc", "hot-coffee"),
    (8, "Starbucks reserve Dark Chocolate Mocha", 0.00, "enter desc", "hot-coffee"),
    (8, "White Chocolate Mocha", 0.00, "enter desc", "hot-coffee"),
    (9, "Veranda", 0.00, "enter desc", "hot-coffee"),
    (9, "Dark Roast", 0.00, "enter desc", "hot-coffee"),
    (9, "Pike Place", 0.00, "enter desc", "hot-coffee"),
    (9, "Decaf Pike", 0.00, "enter desc", "hot-coffee"),
]

menu_drink_hot_tea_subcategory = [
    (1, "Chai Teas", "hot-tea"),
    (2, "Black Teas", "hot-tea"),
    (3, "Green Teas", "hot-tea"),
    (4, "Herbal Teas", "hot-tea"),
]

menu_drink_hot_tea = [
    (1, "Chai Tea Latte", 0.00, "enter desc", "hot-tea"),
    (1, "Chai Tea", 0.00, "enter desc", "hot-tea"),
    (2, "Earl Grey Tea", 0.00, "enter desc", "hot-tea"),
    (2, "Teavana London Fog Tea Latte", 0.00, "enter desc", "hot-tea"),
    (2, "Royal English Breakfast Tea", 0.00, "enter desc", "hot-tea"),
    (2, "Royal English Breakfast Tea Latte", 0.00, "enter desc", "hot-tea"),
    (3, "Emperors Clouds & Mist", 0.00, "enter desc", "hot-tea"),
    (3, "Matcha Tea Latte", 0.00, "enter desc", "hot-tea"),
    (3, "Honey Citrus Mint Tea", 0.00, "enter desc", "hot-tea"),
    (3, "Jade Citrus Mint Brewed Tea", 0.00, "enter desc", "hot-tea"),
    (4, "Mint Majesty", 0.00, "enter desc", "hot-tea"),
    (4, "Peach Tranquility", 0.00, "enter desc", "hot-tea"),
]

menu_drink_hot_drink_subcategory = [
    (1, "Hot Chocolates", "hot-drink"),
    (2, "Juice", "hot-drink"),
    (3, "Steamers", "hot-drink"),
]

menu_drink_hot_drink = [
    (1, "Hot Chocolate", 0.00, "enter desc", "hot-drink"),
    (1, "White Hot Chocolate", 0.00, "enter desc", "hot-drink"),
    (2, "Caramel Apple Spice", 0.00, "enter desc", "hot-drink"),
    (2, "Steamed Apple Juice", 0.00, "enter desc", "hot-drink"),
    (3, "Pumpkin Spice Creme", 0.00, "enter desc", "hot-drink"),
    (3, "Steamed Milk", 0.00, "enter desc", "hot-drink"),
    (3, "Vanilla Creme", 0.00, "enter desc", "hot-drink"),
]

menu_drink_frappuccino_subcategory = [
    (1, "Coffee Frappuccino", "frappuccino-drink"),
    (2, "Creme Frappuccino", "frappuccino-drink"),
]

menu_drink_frappuccino_drink = [
    (1, "Apple Crisp Oatmilk Frappuccino Blended Beverage", 0.00, "enter desc", "frappuccino-drink"),
    (1, "Pumpkin Spice Frappuccino Blended Beverage", 0.00, "enter desc", "frappuccino-drink"),
    (1, "Mocha Cookie Crumble Frappuccino", 0.00, "enter desc", "frappuccino-drink"),
    (1, "Caramel Ribbon Crunch Frappuccino Blended Beverage", 0.00, "enter desc", "frappuccino-drink"),
    (1, "Espresso Frappuccino Blended Beverage", 0.00, "enter desc", "frappuccino-drink"),
    (1, "Caffe Vanilla Frappuccino Blended Beverage", 0.00, "enter desc", "frappuccino-drink"),
    (1, "Caramel Frappuccino Blended Beverage", 0.00, "enter desc", "frappuccino-drink"),
    (1, "Coffee Frappuccino Blended Beverage", 0.00, "enter desc", "frappuccino-drink"),
    (1, "Mocha Frappuccino Blended Beverage", 0.00, "enter desc", "frappuccino-drink"),
    (1, "Java Chip Frappuccino Blended Beverage", 0.00, "enter desc", "frappuccino-drink"),
    (1, "White Chocolate Mocha Frappuccino Blended Beverage", 0.00, "enter desc", "frappuccino-drink"),
    (2, "Apple Crisp Oatmilk Creme Frappuccino Blended Beverage", 0.00, "enter desc", "frappuccino-drink"),
    (2, "Pumpkin Spice Creme Frappuccino Blended Beverage", 0.00, "enter desc", "frappuccino-drink"),
    (2, "Chocolate Cookie Crumble Creme Frappuccino", 0.00, "enter desc", "frappuccino-drink"),
    (2, "Caramel Ribbon Crunch Creme Frappuccino Blended Beverage", 0.00, "enter desc", "frappuccino-drink"),
    (2, "Strawberry Creme Frappuccino Blended Beverage", 0.00, "enter desc", "frappuccino-drink"),
    (2, "Chai Creme Frappuccino", 0.00, "enter desc", "frappuccino-drink"),
    (2, "Double Chocolaty Chip Creme Frappuccino Blended Beverage", 0.00, "enter desc", "frappuccino-drink"),
    (2, "Matcha Creme Frappuccino Blended Beverage", 0.00, "enter desc", "frappuccino-drink"),
    (2, "Vanilla Bean Creme Frappuccino Blended Beverage", 0.00, "enter desc", "frappuccino-drink"),
    (2, "White Chocolate Creme Frappuccino Blended Beverage", 0.00, "enter desc", "frappuccino-drink"),
]

menu_drink_cold_coffee_subcategory = [
    (1, "Cold Brews", "cold-coffee"),
    (2, "Nitro Cold Brews", "cold-coffee"),
    (3, "Iced Americano", "cold-coffee"),
    (4, "Iced Coffees", "cold-coffee"),
    (5, "Iced Shaken Espresso", "cold-coffee"),
    (6, "Iced Flat Whites", "cold-coffee"),
    (7, "Iced Lattes", "cold-coffee"),
    (8, "Iced Macchiatos", "cold-coffee"),
    (9, "Iced Mochas", "cold-coffee"),
]

menu_drink_cold_coffee = [
    (1, "Pumpkin Cream Cold Brew", 0.00, "enter desc", "cold-coffee"),
    (1, "Oleato Golden Foam Cold Brew", 0.00, "enter desc", "cold-coffee"),
    (1, "Cinnamon Caramel Cream Cold Brew", 0.00, "enter desc", "cold-coffee"),
    (1, "Chocolate Cream Cold Brew", 0.00, "enter desc", "cold-coffee"),
    (1, "Salted Caramel Cream Cold Brew", 0.00, "enter desc", "cold-coffee"),
    (1, "Starbucks reserve Cold Brew", 0.00, "enter desc", "cold-coffee"),
    (1, "Starbucks Cold Brew Coffee", 0.00, "enter desc", "cold-coffee"),
    (1, "Vanilla Sweet Cream Cold Brew", 0.00, "enter desc", "cold-coffee"),
    (1, "Starbucks Cold Brea Coffee with Milk", 0.00, "enter desc", "cold-coffee"),
    (2, "Cinnamon Caramel Cream Nitro Cold Brew", 0.00, "enter desc", "cold-coffee"),
    (2, "Nitro Cold Brew", 0.00, "enter desc", "cold-coffee"),
    (2, "Vanilla Sweet Cream Nitro Cold Brew", 0.00, "enter desc", "cold-coffee"),
    (3, "Iced Caffe Amaricano", 0.00, "enter desc", "cold-coffee"),
    (4, "Iced Coffee", 0.00, "enter desc", "cold-coffee"),
    (4, "Iced Coffee Iced Coffee with Milk", 0.00, "enter desc", "cold-coffee"),
    (4, "Iced Espresso", 0.00, "enter desc", "cold-coffee"),
    (5, "Iced Apple Crisp Oatmilk Shaken Espresso", 0.00, "enter desc", "cold-coffee"),
    (5, "Oleato Iced Shaken Espresso with Oatmilk and Toffeenut", 0.00, "enter desc", "cold-coffee"),
    (5, "Iced Toasted Vanilla Oatmilk Shaken Espresso", 0.00, "enter desc", "cold-coffee"),
    (5, "Iced Brown Sugar Oatmilk Shaken Espresso", 0.00, "enter desc", "cold-coffee"),
    (5, "Iced Chocolate Almondmilk Shaken Espresso", 0.00, "enter desc", "cold-coffee"),
    (5, "Iced Shaken Espresso", 0.00, "enter desc", "cold-coffee"),
    (6, "Iced Flat White", 0.00, "enter desc", "cold-coffee"),
    (6, "Iced Honey Almondmilk Flat White", 0.00, "enter desc", "cold-coffee"),
    (7, "Iced Pumpkin Spice Latte", 0.00, "enter desc", "cold-coffee"),
    (7, "Starbucks Reserve Iced Latte", 0.00, "enter desc", "cold-coffee"),
    (7, "Starbucks Reserve Iced Hazlenut Bianco Latte", 0.00, "enter desc", "cold-coffee"),
    (7, "Iced Caffe Latte", 0.00, "enter desc", "cold-coffee"),
    (7, "Iced Cinnamon Dolce Latte", 0.00, "enter desc", "cold-coffee"),
    (7, "Iced Starbucks Blonde Vanilla Latte", 0.00, "enter desc", "cold-coffee"),
    (8, "Iced Apple Crisp Oatmilk Macchiato", 0.00, "enter desc", "cold-coffee"),
    (8, "Iced Caramel Macchiato", 0.00, "enter desc", "cold-coffee"),
    (9, "Iced White Chocolate Mocha", 0.00, "enter desc", "cold-coffee"),
    (9, "Iced Caffe Mocha", 0.00, "enter desc", "cold-coffee"),
    (9, "Starbucks Reserve Iced Dark Chocolate Mocha", 0.00, "enter desc", "cold-coffee"),
]

menu_drink_iced_tea_subcategory = [
    (1, "Bottled Teas", "iced-tea"),
    (2, "Iced Black Teas", "iced-tea"),
    (3, "Iced Chai Teas", "iced-tea"),
    (4, "Iced Green Teas", "iced-tea"),
    (5, "Iced Herbal Teas", "iced-tea"),
]

menu_drink_iced_tea = [
    (1, "Teavana Sparkling Unsweetened Peach Nectarine Green Tea", 0.00, "enter desc", "iced-tea"),
    (1, "Teavana Mango Black Tea", 0.00, "enter desc", "iced-tea"),
    (2, "Iced Black Tea", 0.00, "enter desc", "iced-tea"),
    (2, "Iced Black Tea Lemonade", 0.00, "enter desc", "iced-tea"),
    (2, "Iced Royal English Breakfast Tea Latte", 0.00, "enter desc", "iced-tea"),
    (2, "Iced London Fog Tea Latte", 0.00, "enter desc", "iced-tea"),
    (3, "Iced Pumpkin Cream Chai Tea Latte", 0.00, "enter desc", "iced-tea"),
    (3, "Iced Chai Tea Latte", 0.00, "enter desc", "iced-tea"),
    (4, "Iced Peach Green Tea", 0.00, "enter desc", "iced-tea"),
    (4, "Iced Peach Green Tea Lemonade", 0.00, "enter desc", "iced-tea"),
    (4, "Iced Matcha Tea Latte", 0.00, "enter desc", "iced-tea"),
    (4, "Iced Green Tea", 0.00, "enter desc", "iced-tea"),
    (4, "Iced Green Tea Lemonade", 0.00, "enter desc", "iced-tea"),
    (4, "Iced Matcha Lemonade", 0.00, "enter desc", "iced-tea"),
    (5, "Iced Passion Tango Tea", 0.00, "enter desc", "iced-tea"),
    (5, "Iced Passion Tango Tea Lemonade", 0.00, "enter desc", "iced-tea"),

]

menu_items =\
    menu_drink_oleato +\
    menu_drink_hot_coffee +\
    menu_drink_hot_tea +\
    menu_drink_hot_drink +\
    menu_drink_frappuccino_drink +\
    menu_drink_cold_coffee +\
    menu_drink_iced_tea

menu_items_sub =\
    menu_drink_hot_coffee_subcategory +\
    menu_drink_hot_tea_subcategory +\
    menu_drink_hot_drink_subcategory +\
    menu_drink_frappuccino_subcategory +\
    menu_drink_cold_coffee_subcategory +\
    menu_drink_iced_tea_subcategory

cursor.executemany('''
    INSERT INTO menu_item_details (item_id, name, price, description, subcategory)
    VALUES (?, ?, ?, ?, ?)
''', menu_items)

cursor.executemany('''
    INSERT INTO menu_item_subcategories (item_id, name, subcategory)
    VALUES (?, ?, ?)
''', menu_items_sub)

connection.commit()
connection.close()

print("Starbucks menu database created and populated with your data.")
