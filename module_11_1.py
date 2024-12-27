import matplotlib.pyplot as plt
import requests
import json


# Библиотека `requests` значительно упрощает работу с HTTP-запросами в Python. Она позволяет быстро и просто отправлять
# запросы, получать и обрабатывать ответы, а также управлять заголовками и параметрами.
#  Основные возможности библиотеки requests:
#  Отправка GET-запросов,GET-запросы используются для получения данных с сервера.

response = requests.get('https://api.github.com')
print(response.status_code)  # Код статуса ответа
print(response.json())  # Данные в формате JSON

# Отправка POST-запросов,POST-запросы используются для отправки данных на сервер.
data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', data=data)
print(response.json())  # Выводим ответ сервера

#  Передача параметров в запросе,Параметры можно передавать в URL.
params = {'search': 'Python', 'page': 1}
response = requests.get('https://httpbin.org/get', params=params)
print(response.url)  # URL с параметрами
print(response.json())

# Работа с заголовками, Можно добавлять пользовательские заголовки к запросам.
headers = {'Authorization': 'Bearer yourtokenhere'}
response = requests.get('https://api.github.com/user', headers=headers)
print(response.json())

#  Обработка ошибок, Библиотека позволяет обрабатывать возможные ошибки при выполнении запроса.
try:
       response = requests.get('https://api.github.com/nonexistent')
       response.raise_for_status() # Проверка на ошибки
except requests.exceptions.HTTPError as err:
       print(f'Ошибка: {err}')

#  Отправка данных в формате JSON,Можно отправлять данные в формате JSON, указывая заголовок.
data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', json=data)
print(response.json())


# Matplotlib Основные возможности:
# Создание визуализаций данных (графики, диаграммы и т.д.).
# Настройка внешнего вида графиков (маркировка, цвета, подписи).
# Сохранение графиков в различных форматах (PNG, PDF и др.).
# Пример данных
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

#Создание графика
plt.plot(x, y, marker='o')

# Настройка заголовка и подписей
plt.title('Пример графика')
plt.xlabel('X')
plt.ylabel('Y')

#Отображение графика
plt.show()

#Сохранение графика
plt.savefig('graph.png')
