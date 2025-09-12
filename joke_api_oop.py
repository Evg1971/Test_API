# Импортируем библиотеку requests для работы с HTTP-запросами
import requests

class TestCreateJoke:
    def test_create_random_joke(self, category):
        self.category = category
        url = f"https://api.chucknorris.io/jokes/random?category={self.category}"

        try:
            # Отправляем GET-запрос по указанному URL
            response = requests.get(url)

            # Выводим URL, по которому отправляем запрос
            print(f"Отправляем запрос по URL: {url}")

            # Выводим статус-код ответа
            print(f"Статус код ответа: {response.status_code}")

            # Проверяем, что статус-код ответа равен 200 (успешный запрос)
            assert response.status_code == 200, "Неверный код - ожидаемый код: 200"
            print("Статус код верный")

            # Проверяем, что ответ содержит данные в формате JSON
            data = response.json()
            print(f"Ответ от сервера: {data}")

            # Проверяем, что категория шутки соответствует запрошенной
            assert self.category in data['categories'], f"Ожидаемая категория: {self.category}"

            # Проверяем, что в теле шутки содержится имя "Chuck"
            assert 'Chuck' in data['value'], "Имя 'Chuck' не найдено в теле шутки"

            # Выводим саму шутку на печать
            print(f"Шутка про Чак Норриса из категории {self.category}:\n {data['value']}")


        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return False
        except KeyError as e:
            print(f"Ошибка: отсутствует ключ {e} в ответе API")
            return False
        except AssertionError as e:
            print(f"Проверка не пройдена: {e}")
            return False

test_joke = TestCreateJoke()
test_joke.test_create_random_joke('career')