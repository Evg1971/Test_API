# Импорт библиотеки requests для выполнения HTTP-запросов
import requests


class PlaceAPIClient:
    """Класс для взаимодействия с API мест."""

    def __init__(self):
        """Инициализация клиента с базовым URL и ключом."""
        # Базовый URL API
        self.base_url = 'https://rahulshettyacademy.com'
        # Параметр ключа для аутентификации в API
        self.key = '?key=qaclick123'
        # Путь для создания нового места (POST-запрос)
        self.post_resource = '/maps/api/place/add/json'
        # Путь для получения информации о месте (GET-запрос)
        self.get_resource = '/maps/api/place/get/json'

    def create_place(self, payload):
        # Формирование полного URL для POST-запроса
        post_url = self.base_url + self.post_resource + self.key
        # Отправка POST-запроса с переданными данными (payload)
        response = requests.post(post_url, json=payload)
        # Возврат ответа сервера в формате JSON
        return response.json()

    def get_place(self, place_id):
        # Формирование полного URL для GET-запроса с указанием place_id
        get_url = self.base_url + self.get_resource + self.key + "&place_id=" + place_id
        # Отправка GET-запроса
        response = requests.get(get_url)
        # Возврат объекта ответа (включает статус-код, заголовки и тело ответа)
        return response


def test_place_api_workflow():
    """
    Тестовый сценарий:
    1. Создаёт 5 мест через POST-запросы.
    2. Сохраняет их идентификаторы (place_id) в текстовый файл.
    3. Читает place_id из файла и проверяет их существование через GET-запросы.
    """
    # Создание экземпляра клиента для работы с API
    client = PlaceAPIClient()
    # Список для хранения идентификаторов созданных мест
    place_ids = []

    # 1. Создание 5 мест и сбор их идентификаторов (place_id)
    for i in range(5):
        # Формирование данных для создания нового места
        payload = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": f"Frontline house {i}",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": ["shoe park", "shop"],
            "website": "http://google.com",
            "language": "French-IN"
        }
        # Отправка запроса на создание места
        response = client.create_place(payload)
        # Добавление полученного place_id в список
        place_ids.append(response["place_id"])
        # Вывод информации о созданном месте
        print(f"Создано место с place_id: {response['place_id']}")

    # 2. Сохранение place_id в текстовый файл
    with open("place_ids.txt", "w") as f:
        # Запись всех place_id в файл, каждый с новой строки
        f.write("\n".join(place_ids))
    print("Список place_id сохранён в файл place_ids.txt")

    # 3. Чтение place_id из файла и проверка их существования
    with open("place_ids.txt", "r") as f:
        # Чтение всех строк из файла и удаление символов новой строки
        saved_place_ids = [line.strip() for line in f.readlines()]
        # Вывод списка прочитанных place_id для отладки
        print(f"Создан список {saved_place_ids} с place_id")

    # Проверка существования каждого места по его place_id
    for place_id in saved_place_ids:
        # Отправка GET-запроса для проверки существования места
        response = client.get_place(place_id)
        # Проверка, что статус-код ответа равен 200 (OK)
        assert response.status_code == 200
        # Вывод сообщения об успешной проверке
        print(f"Место с place_id {place_id} существует")


# Запуск тестового сценария
test_place_api_workflow()
# Вывод сообщения об успешном завершении теста
print("Тест прошёл успешно")
