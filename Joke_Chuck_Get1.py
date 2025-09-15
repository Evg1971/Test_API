import requests
from requests.exceptions import RequestException


class TestChuckGet1:
    """Класс для работы с API Chuck Norris"""

    def get_all_categories(self):
        """Получает список всех доступных категорий шуток"""
        try:
            # Отправляем GET-запрос для получения списка категорий
            response = requests.get("https://api.chucknorris.io/jokes/categories")
            return response.json()
        except ValueError as e:
            print(f"Ошибка декодирования JSON: {e}")
        except RequestException as e:
            print(f"Ошибка запроса: {e}")
        return []  # Возвращаем пустой список в случае ошибки

    def get_joke_by_category(self, category):
        """Получает случайную шутку из указанной категории"""
        try:
            # Сохраняем переданную категорию как атрибут экземпляра
            self.category = category
            # Формируем URL с указанной категорией
            url = f"https://api.chucknorris.io/jokes/random?category={self.category}"
            # Отправляем GET-запрос для получения шутки
            response = requests.get(url)
            return response.json()
        except ValueError as e:
            print(f"Ошибка декодирования JSON для категории {self.category}: {e}")
        except RequestException as e:
            print(f"Ошибка запроса для категории {self.category}: {e}")
        return None  # Возвращаем None в случае ошибки

    def test_get_jokes_from_all_categories(self):
        """
        Основной метод, который:
        1. Получает все доступные категории
        2. Для каждой категории получает и выводит случайную шутку
        """
        try:
            # Получаем список всех категорий
            categories = self.get_all_categories()

            # Выводим информацию о найденных категориях
            print(f"Найдено: {len(categories)} категорий")
            print("Список категорий:", categories)

            # Для каждой категории получаем и выводим шутку
            for category in categories:
                try:
                    print(f"\nПолучение шутки из категории: {category}")

                    # Получаем данные шутки
                    joke_data = self.get_joke_by_category(category)

                    assert joke_data is not None, f"Не удалось получить шутку для категории {category}"

                    # Выводим текст шутки
                    print(f"Шутка: {joke_data['value']}")

                    # Проверяем наличие имени "Chuck" в шутке
                    assert "Chuck" in joke_data['value'], f"Внимание! В шутке не найдено имя 'Chuck'"

                except (KeyError, TypeError) as e:
                    print(f"Ошибка при обработке данных для категории {category}: {e}")

        except RequestException as e:
            print(f"Ошибка запроса : {e}")


# Создаем экземпляр класса
Test_1 = TestChuckGet1()

# Запускаем тестовый метод для получения шуток из всех категорий
Test_1.test_get_jokes_from_all_categories()
