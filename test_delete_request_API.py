import requests

from Delete_request import PlaceAPIClient


def test_delete_and_filter_places():
    """
    Тестовый сценарий:
    1. Удаляет 2-й и 4-й place_id из файла (логически, через DELETE запрос).
    2. Проверяет существование всех мест через GET-запросы.
    3. Сохраняет только существующие place_id в новый файл.
    """
    client = PlaceAPIClient()
    # 1. Чтение place_id из файла
    place_ids = client.read_place_ids_from_file("place_ids.txt")
    if not place_ids or len(place_ids) < 5:
        print("Не удалось прочитать place_id из файла или недостаточно данных.")
        return
    print(f"Прочитанные place_id: {place_ids}")
    # 2. Логическое удаление 2-го и 4-го place_id (через DELETE запрос)
    for index in [1, 3]:  # Индексы 1 и 3 соответствуют 2-му и 4-му элементам
        place_id = place_ids[index]
        print(f"Удаление place_id: {place_id}")
        try:
            response = client.delete_place(place_id)
            if response.status_code == 200:
                print(f"Место с place_id {place_id} успешно удалено логически.")
            else:
                print(f"Не удалось удалить место с place_id: {place_id}")
        except requests.exceptions.HTTPError as e:
            print(f"Ошибка при удалении place_id {place_id}: {e}")
    # 3. Проверка существования всех мест
    existing_places = client.filter_existing_places(place_ids)
    print(f"Существующие place_id: {existing_places}")
    # 4. Сохранение только существующих place_id в новый файл
    client.save_place_ids_to_file("existing_places.txt", existing_places)


# Запуск теста
test_delete_and_filter_places()
print("Тест завершён успешно")