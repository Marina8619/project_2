import sqlite3

# Создание подключения к базе данных или ее создание, если не существует
conn = sqlite3.connect('inventory_management.db')
cursor = conn.cursor()

# Создание таблицы "Категории товаров"
cursor.execute('''
CREATE TABLE IF NOT EXISTS ProductCategories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
''')

# Создание таблицы "Характеристики товаров"
cursor.execute('''
CREATE TABLE IF NOT EXISTS ProductCharacteristics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
''')

# Создание таблицы "Товары"
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER,
    characteristic_id INTEGER,
    name TEXT,
    code TEXT UNIQUE,
    expiration_date DATE,
    FOREIGN KEY (category_id) REFERENCES ProductCategories(id),
    FOREIGN KEY (characteristic_id) REFERENCES ProductCharacteristics(id)
)
''')

# Создание таблицы "Склады"
cursor.execute('''
CREATE TABLE IF NOT EXISTS Warehouses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address TEXT,
    name TEXT,
    location_text TEXT,
    location_coordinates TEXT
)
''')

# Создание таблицы "Клиенты"
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    contact_info TEXT
)
''')

# Создание таблицы "Заказы"
cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    date DATETIME,
    FOREIGN KEY (client_id) REFERENCES Clients(id)
)
''')

# Создание таблицы "Товары в Заказе"
cursor.execute('''
CREATE TABLE IF NOT EXISTS OrderItems (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (order_id) REFERENCES Orders(id),
    FOREIGN KEY (product_id) REFERENCES Products(id)
)
''')

# Создание таблицы "Документы"
cursor.execute('''
CREATE TABLE IF NOT EXISTS Documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    content BLOB
)
''')

# Сохранение изменений и закрытие подключения к базе данных
conn.commit()
conn.close()

print("База данных успешно создана.")