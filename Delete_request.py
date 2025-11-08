import requests


class PlaceAPIClient:
    def __init__(self):
        """Инициализация клиента API"""
        self.base_url = 'https://rahulshettyacademy.com'
        self.key = '?key=qaclick123'
        self.get_resource = '/maps/api/place/get/json'
        self.delete_resource = '/maps/api/place/delete/json'

    def delete_place(self, place_id):
        """Удаляет место по его идентификатору"""
        delete_url = self.base_url + self.delete_resource + self.key
        payload = {"place_id": place_id}
        response = requests.delete(delete_url, json=payload)
        response.raise_for_status()
        return response

    def get_place(self, place_id):
        """Получает информацию о месте по его идентификатору"""
        get_url = self.base_url + self.get_resource + self.key + f'&place_id={place_id}'
        response = requests.get(get_url)
        response.raise_for_status()
        return response

    @staticmethod
    def read_place_ids_from_file(filename):
        """Читает идентификаторы мест из текстового файла"""
        try:
            with open(filename, "r") as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print(f"Ошибка: файл {filename} не найден.")
            return []

    def filter_existing_places(self, place_ids):
        """Фильтрует существующие места из списка идентификаторов.
        """
        existing_places = []
        for place_id in place_ids:
            try:
                response = self.get_place(place_id)
                assert response.status_code == 200, f"Место с place_id {place_id} не существует."
                existing_places.append(place_id)
                print(f"Место с place_id {place_id} существует.")
            except requests.exceptions.HTTPError as e:
                print(f"Ошибка при проверке place_id {place_id}: {e}")
        return existing_places

    @staticmethod
    def save_place_ids_to_file(filename, place_ids):
        """Сохраняет идентификаторы мест в текстовый файл"""
        try:
            with open(filename, "w") as f:
                f.write("\n".join(place_ids))
            print(f"Идентификаторы мест успешно сохранены в файл {filename}.")
        except Exception as e:
            print(f"Ошибка при записи в файл {filename}: {e}")
