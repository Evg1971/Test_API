# Импортируем библиотеку requests для работы с HTTP-запросами
import requests

# URL для получения случайной шутки
url = "https://api.chucknorris.io/jokes/random"

# Выводим URL, по которому отправляем запрос
print(f"Отправляем запрос по URL: {url}")

# Отправляем GET-запрос по указанному URL
result = requests.get(url)

# Выводим статус-код ответа
print(f"Статус код ответа: {result.status_code}")

# Dыводим сообщения в зависимости от статуса ответа
print("Успех! Статус код верный!" if result.status_code == 200
      else "Ошибка! Статус код неверный")

# Устанавливаем кодировку ответа в UTF-8 для корректного отображения текста
result.encoding = "utf-8"

# Выводим текст ответа в формате JSON только если статус код равен 200
if result.status_code == 200:
    print(f"Ответ от сервера: {result.text}")
else:
    print("Ответ от сервера не выведен из-за ошибки.")