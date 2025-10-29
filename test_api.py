import requests
import allure
from config import HEADERS, base_api_url


@allure.title("Поиск фильмов по 2025 году")
@allure.description("Ввод год")
@allure.severity("critical")
def test_movies_2025():
    with allure.step("отправить запрос на фильмы 2025г"):
        response = requests.get(base_api_url+"movie?page=1&limit=10&type=movie&year=2025",
                                headers=HEADERS)
    with allure.step("проверить код ответа"):
        assert response.status_code == 200
    with allure.step("проверить тело ответа"):
        assert response.json()["docs"][0]["name"] == "Кинолюбители"


@allure.title("Поиск фильма по id")
@allure.description("Ввод id")
@allure.severity("critical")
def test_movies_id():
    with allure.step("отправить запрос фильма по id"):
        response = requests.get(base_api_url+"movie/1355059",
                                headers=HEADERS)
    with allure.step("проверить код ответа"):
        assert response.status_code == 200
    with allure.step("проверить тело ответа"):
        assert response.json()["name"] == "Беспринципные"


@allure.title("Поиск актера по имени и фамилии")
@allure.description("Ввод имени и фамилии")
@allure.severity("critical")
def test_movies_actor():
    with allure.step("отправить запрос на актера Джонни Депп"):
        response = requests.get(base_api_url+"person/search?query='Джонни Депп'",
                                headers=HEADERS)
    with allure.step("проверить код ответа"):
        assert response.status_code == 200
    with allure.step("проверить тело ответа"):
        assert response.json()["docs"][0]["name"] == "Джонни Депп"


@allure.title("Поиск на названию фильма")
@allure.description("Ввод название фильма")
@allure.severity("critical")
def test_movies_name():
    with allure.step("отправить запрос на название фильма 'Форсаж'"):
        response = requests.get(base_api_url+"movie/search?page=1&limit=10&query=Форсаж",
                                headers=HEADERS)
    with allure.step("проверить код ответа"):
        assert response.status_code == 200
    with allure.step("проверить тело ответа"):
        assert response.json()["docs"][0]["name"] == "Форсаж"


@allure.title("Поиск списка жанров")
@allure.description("Ввод жанра")
@allure.severity("critical")
def test_movies_style():
    with allure.step("отправить запрос на жанр комедия"):
        response = requests.get(base_api_url+"movie?year=2020&genres.name=комедия",
                                headers=HEADERS)
    with allure.step("проверить код ответа"):
        assert response.status_code == 200
    with allure.step("проверить тело ответа"):
        assert response.json()[
            "docs"][0]["alternativeName"] == "Christmas Zombies"
