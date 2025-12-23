Локальный запуск
----------------
***1. Установка зависимостей***
```commandline
pip install -r requirements.txt
```
***2. Запуск тестов***
```commandline
pytest -v
```
***3. Запуск с Allure***
```commandline
pytest --alluredir=allure-results
allure serve allure-results
```

Запуск с Docker
---------------
***1. Сборка образа***
```commandline
docker build -t saucedemo-tests .
```
***2. Запуск контейнера***
```commandline
docker run --rm saucedemo-tests
```
***3. Получение Allure-отчета***
```commandline
docker run --rm \
  -v $(pwd)/allure-results:/app/allure-results \
  saucedemo-tests
```
После этого:
```commandline
allure serve allure-results
```