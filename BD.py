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

# Функция для добавления новой категории товаров
def add_product_category(name):
    cursor.execute('INSERT INTO ProductCategories (name) VALUES (?)', (name,))
    conn.commit()

# Функция для добавления новой характеристики товаров
def add_product_characteristic(name):
    cursor.execute('INSERT INTO ProductCharacteristics (name) VALUES (?)', (name,))
    conn.commit()

# Функция для добавления нового товара
def add_product(category_id, characteristic_id, name, code, expiration_date):
    cursor.execute('''
    INSERT INTO Products (category_id, characteristic_id, name, code, expiration_date)
    VALUES (?, ?, ?, ?, ?)
    ''', (category_id, characteristic_id, name, code, expiration_date))
    conn.commit()

# Функция для добавления нового склада
def add_warehouse(address, name, location_text, location_coordinates):
    cursor.execute('INSERT INTO Warehouses (address, name, location_text, location_coordinates) VALUES (?, ?, ?, ?)',
                   (address, name, location_text, location_coordinates))
    conn.commit()

# Функция для добавления нового клиента
def add_client(name, contact_info):
    cursor.execute('INSERT INTO Clients (name, contact_info) VALUES (?, ?)', (name, contact_info))
    conn.commit()

# Функция для добавления нового заказа
def add_order(client_id, date):
    cursor.execute('INSERT INTO Orders (client_id, date) VALUES (?, ?)', (client_id, date))
    conn.commit()

# Функция для добавления товара в заказ
def add_order_item(order_id, product_id, quantity):
    cursor.execute('INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (?, ?, ?)', (order_id, product_id, quantity))
    conn.commit()

# Функция для добавления нового документа
def add_document(type, content):
    cursor.execute('INSERT INTO Documents (type, content) VALUES (?, ?)', (type, content))
    conn.commit()

# Примеры использования функций для добавления данных
add_product_category('Электроника')
add_product_characteristic('Цвет')
add_product(1, 1, 'Смартфон', 'ABC123', '2023-12-31')
add_warehouse('Адрес склада', 'Склад №1', 'Расположение', 'Координаты')
add_client('Иванов Иван', 'Телефон: 123-456, Email: ivanov@example.com')
add_order(1, '2023-10-02')
add_order_item(1, 1, 2)
add_document('Счет', 'Содержание счета...')

# Закрытие подключения к базе данных
conn.close()


print("База данных успешно создана.")
