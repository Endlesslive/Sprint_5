import random
import string

def generate_email():
    """
    Генерирует случайный email в формате логин@домен.
    
    Returns:
        str: Случайный email адрес
    """
    username_length = random.randint(8, 15)
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) 
                      for _ in range(username_length))
    
    domains = ['yandex.ru', 'gmail.com', 'mail.ru', 'example.com']
    domain = random.choice(domains)
    
    return f"{username}@{domain}"

def generate_password(length=6):
    """
    Генерирует случайный пароль заданной длины.
    
    Args:
        length (int): Длина пароля (минимум 6 символов)
    
    Returns:
        str: Случайный пароль
    """
    if length < 6:
        length = 6
    
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def generate_name():
    """
    Генерирует случайное имя.
    
    Returns:
        str: Случайное имя
    """
    names = ['Анастасия', 'Иван', 'Мария', 'Алексей', 'Елена', 
             'Дмитрий', 'Ольга', 'Сергей', 'Татьяна', 'Михаил']
    
    return random.choice(names)
