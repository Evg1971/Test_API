import requests
from requests.exceptions import RequestException


class TestChuckGet2:
    """Класс для работы с API Chuck Norris"""

    @staticmethod
    def get_all_categories():
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

    @staticmethod
    def get_joke_by_category(category):
        """Получает случайную шутку из указанной категории"""
        try:
            # Формируем URL с указанной категорией
            url = f"https://api.chucknorris.io/jokes/random?category={category}"
            # Отправляем GET-запрос для получения шутки
            response = requests.get(url)
            return response.json()
        except ValueError as e:
            print(f"Ошибка декодирования JSON для категории {category}: {e}")
        except RequestException as e:
            print(f"Ошибка запроса для категории {category}: {e}")
        return None  # Возвращаем None в случае ошибки

    def run_category_test(self):
        """Основной метод теста, который:
        1. Запрашивает категорию у пользователя
        2. Получает все доступные категории
        3. Проверяет, что выбранная категория существует
        4. Получает шутку для выбранной категории
        5. Проверяет корректность ответа"""

        print("Тестирование API Chuck Norris")

        try:
            # Шаг 1: Запрос категории у пользователя
            user_category = input(
                "\nВведите категорию для получения шутки (например: animal, career, food): ").strip().lower()
            # Шаг 2: Получение всех категорий
            print("\nПолучение списка доступных категорий...")
            categories = self.get_all_categories()
            # Выводим информацию о найденных категориях
            print(f"Найдено: {len(categories)} категорий")
            print("Список категорий:", categories)

            # Шаг 3: Проверка существования выбранной категории
            assert user_category in categories, f"Категория '{user_category}' не найдена в списке доступных категорий"
            print(f"\nКатегория '{user_category}' найдена в доступных категориях")

            # Шаг 4: Получение шутки для выбранной категории
            print(f"\nПолучение шутки из категории '{user_category}'...")
            joke_data = self.get_joke_by_category(user_category)
            assert joke_data is not None, f"Не удалось получить шутку для категории {user_category}"
            # Выводим текст шутки
            print(f"Шутка: {joke_data['value']}")
            # Проверяем наличие имени "Chuck" в шутке
            assert "Chuck" in joke_data['value'], f"Внимание! В шутке не найдено имя 'Chuck'"
            print("Все проверки пройдены успешно!")
        except AssertionError as e:
            print(f"\nОшибка проверки: {str(e)}")
        except ValueError as e:
            print(f"\nОшибка значения: {str(e)}")
        except KeyError as e:
            print(f"\nОшибка доступа к данным: {str(e)}")
        except TypeError as e:
            print(f"\nОшибка типа данных: {str(e)}")
        except RequestException as e:
            print(f"\nОшибка HTTP-запроса: {str(e)}")


tester = TestChuckGet2()
tester.run_category_test()
