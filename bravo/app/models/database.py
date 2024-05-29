import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

conn = sqlite3.connect('db/database.db')
cursor = conn.cursor()

# Функция регистрации пользователя
def register_user(username, password):
    # Проверяем, существует ли пользователь с таким именем
    cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
    if cursor.fetchone()[0] > 0:
        return False, "Пользователь с таким именем уже существует"

    # Хешируем пароль
    hashed_password = generate_password_hash(password)

    # Добавляем нового пользователя в базу данных
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        return True, "Регистрация выполнена успешно"
    except sqlite3.IntegrityError:
        return False, "Ошибка при добавлении пользователя"

# Функция аутентификации пользователя
def authenticate_user(username, password):
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if result is None:
        return False, "Пользователь не найден"
    hashed_password = result[0]
    if check_password_hash(hashed_password, password):
        return True, "Аутентификация успешна"
    else:
        return False, "Неверный пароль"

# Пример использования
success, message = register_user('newuser', 'mypassword')
if success:
    print(message)
else:
    print(message)

success, message = authenticate_user('newuser', 'mypassword')
if success:
    print(message)
else:
    print(message)

conn.close()
