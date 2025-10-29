Добрый день!
Дипломный проект по автотестированию выполнен по сайту и API "Кинопоиск"
https://www.kinopoisk.ru
https://api.kinopoisk.dev

Выполнены  5 UI тестов и 5 API тестов

Проект поддерживает запуск автотестов в трех режимах:
запуск только UI-тестов,
запуск только API-тестов,
запуск всех тестов.

#команды для запуска тестов

pytest test_ui.py --alluredir allure-result запуск ui тестов

pytest test_api.py --alluredir allure-result запуск API тестов

pytest --alluredir allure-result запуск всех тестов

Подключены зависимости:
selenium,
requests,
pytest,
allure

Использованы шаги 
allure.step


#Как провести тестирование с allure

Откройте терминал и перейдите к рабочей директории (diplom/test):
cd test

Запустите тесты и укажите путь к каталогу результатов тестирования:
python -m pytest --alluredir allure-result


Команда ниже запускает Allure и конвертирует результаты теста в отчет:
allure serve allure-results

#проверен код на соответствие PEP8 autopep8 --in-place --recursive .

ссылка на финальный проект по ручному тестированию
https://na-sa-78.yonote.ru/share/2cb3bc8f-4225-4f8f-b530-554ceee5adfa

