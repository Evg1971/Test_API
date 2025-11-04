from Put_request import PlaceAPIClient

def test_update_place():
    """Тест для проверки успешного обновления адреса места через PUT-запрос."""

    # Инициализация клиента API
    client = PlaceAPIClient()

    # Данные для создания нового места
    payload = {
        "location": {
            "lat": -38.383494,  # Широта
            "lng": 33.427362    # Долгота
        },
        "accuracy": 50,          # Точность координат
        "name": "Frontline house",  # Название места
        "phone_number": "(+91) 983 893 3937",  # Номер телефона
        "address": "29, side layout, cohen 09",  # Адрес места
        "types": ["shoe park", "shop"],  # Типы места
        "website": "http://google.com",  # Веб-сайт
        "language": "French-IN"  # Язык
    }

    # Создание нового места и получение его ID
    create_response = client.create_place(payload)
    place_id = create_response.get('place_id')
    print(f"Создано место с place_id: {place_id}")

    # Новый адрес для обновления
    new_address = '22 ulica Pobeda, RU'
    print(f"Обновление адреса на '{new_address}'")

    # Обновление адреса места с помощью PUT-запроса
    update_response = client.update_place(place_id, new_address)

    # Проверка, что PUT-запрос выполнен успешно (статус-код 200)
    assert update_response.status_code == 200, (
        f"Ожидался статус-код 200, а получен {update_response.status_code}")

    print(f"Успешный ответ на PUT-запрос: {update_response.status_code}")

    # Получение обновленного места
    get_data = client.get_place(place_id).json()

    # Проверка, что адрес действительно обновился на новый
    assert get_data.get('address') == new_address, (
        f"Адрес не обновился! Ожидалось: {new_address}, получено: {get_data.get('address')}"
    )
    print("Адрес места обновлен корректно.")

# Запуск теста
test_update_place()
print("Тест завершен успешно")