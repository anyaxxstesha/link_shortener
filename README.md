# Для запуска:
1. Ввести команду "pip install -r requirements.txt"
2. Ввести команду "python manage.py runserver"

# Эндпоинты:

---


```
POST /links/
```
```
Возвращает все ссылки постранично
```
---
```
POST /links/create/
```
```
Возвращает форму для генерации короткой ссылки
```
---
```
GET /EX12pl/
```
```
Перенаправляет на исходную страницу, соответствующую данной укороченной ссылке
```
