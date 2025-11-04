import requests

class PlaceAPIClient:
    """
    Класс для взаимодействия с API мест на платформе Rahul Shetty Academy.
    Предоставляет методы для создания, получения и обновления информации о местах.
    """

    def __init__(self):
        """Инициализация клиента API. Устанавливает базовые параметры для запросов:
        базовый URL, ключ API и ресурсы."""
        self.base_url = 'https://rahulshettyacademy.com'  # Базовый URL API
        self.key = '?key=qaclick123'  # Ключ для доступа к API
        self.get_resource = '/maps/api/place/get/json'  # Ресурс для получения информации о месте
        self.post_resource = '/maps/api/place/add/json'  # Ресурс для создания нового места
        self.put_resource = '/maps/api/place/update/json'  # Ресурс для обновления информации о месте

    def create_place(self, payload):
        """Создает новое место на основе переданных данных."""
        # Формирование URL для создания места
        post_url = self.base_url + self.post_resource + self.key
        # Отправка POST-запроса на создание места
        response = requests.post(post_url, json=payload)
        # Проверка на наличие ошибок в ответе
        response.raise_for_status()
        # Возврат JSON-ответа
        return response.json()

    def get_place(self, place_id):
        """Получает информацию о месте по его идентификатору"""
        # Формирование URL для получения информации о месте
        get_url = self.base_url + self.get_resource + self.key + f"&place_id={place_id}"
        # Отправка GET-запроса для получения информации о месте
        response = requests.get(get_url)
        # Проверка на наличие ошибок в ответе
        response.raise_for_status()
        # Возврат объекта ответа
        return response

    def update_place(self, place_id, new_address):
        """ Обновляет адрес места по его идентификатору."""
        # Формирование URL для обновления информации о месте
        put_url = self.base_url + self.put_resource + self.key
        print(f"URL для обновления: {put_url}")

        # Формирование данных для обновления
        payload = {
            "place_id": place_id,  # Идентификатор места
            "address": new_address,  # Новый адрес
            "key": 'qaclick123'  # Ключ для доступа к API
        }

        # Отправка PUT-запроса для обновления адреса
        response = requests.put(put_url, json=payload)
        # Проверка на наличие ошибок в ответе
        response.raise_for_status()
        # Возврат объекта ответа
        return response