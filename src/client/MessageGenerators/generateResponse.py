def generate_response(data):
    return f"Назва: {data['name']} \nКількість: {data['quantity']} \nСрокі: {data['date']}\nДодаткова інформація: {data['info']}\n\nЯкщо все правильно натисніть /save.\nЯкщо ви хочете щось змінити натисніть /change."