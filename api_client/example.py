from client import NewsAPIClient


TOKEN = 'd896359f93f3e4eeafaf589f3240012b91ea41d9'

client = NewsAPIClient(
    base_url='http://127.0.0.1:8000',
    token=TOKEN
)


print('СПИСОК НОВОСТЕЙ')
print(client.get_news())

print('\nСОЗДАНИЕ НОВОСТИ')

new_news = client.create_news(
    title='Новость через API',
    summary='Создано через requests',
    content='Это тестовая новость, созданная через REST API и Python client module.'
)

print(new_news)

print('\nОДНА НОВОСТЬ')
print(client.get_news(1))