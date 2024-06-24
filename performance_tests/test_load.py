from locust import HttpUser, TaskSet, task, between, events


# для запуска кода устанавливаем библиотеку locust
# запускаем через locust -f performance_tests\test_load.py --host http://sitename
# открываем веб интерфейс http://localhost:8089
# выбираем нагрузку: Number of users 1000, Ramp up 10. Нажмем старт.

# так же можно запустить в хедлесс режиме без использования веб интерфейса
# locust -f performance_tests\test_load.py --headless --host http://sitename -u 1000 -r 10 --run-time 2m

# Отправляем POST-запрос к эндпоинту /calculate с JSON-пейлоадом, содержащим данные: числитель и знаменатель
# Если код 200, т.е. страница доступна и нет проблем, проверяем содержимое если нет ошибок и ответ число флоат
# в это случае вызов считается успешным.

class CalculatorTest(TaskSet):
    @task
    def divide(self):
        headers = {'Content-Type': 'application/json'}
        payload = {
            "numerator": "10",
            "denominator": "2"
        }
        with self.client.post("/calculate", json=payload, headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                data = response.json()
                if data["error"] == "" and isinstance(data["answer"], float):
                    response.success()
                else:
                    response.failure("Invalid response content") # в ином случае вызов неудачный
            else:
                response.failure(f"Unexpected status code: {response.status_code}") # при коде отличном от 200, так же
                # вызов считается неудачный


class WebsiteUser(HttpUser):
    tasks = [CalculatorTest]
    wait_time = between(1, 2)


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new test is starting")


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("A new test is ending")

