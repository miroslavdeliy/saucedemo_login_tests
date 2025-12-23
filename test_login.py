import allure
from pages.login_page import LoginPage


# URL и сообщения об ошибках
BASE_URL = 'https://www.saucedemo.com/'
INCORRECT_PASSWORD_ERROR_MESSAGE =\
    ("Epic sadface: Username and password"
     " do not match any user in this service")
LOCKED_USER_MESSAGE = "Epic sadface: Sorry, this user has been locked out."
EMPTY_USER_MESSAGE = "Epic sadface: Username is required"


@allure.epic("Авторизация на сайте Saucedemo")
@allure.feature("Функционал логина")
class TestLogin:

    # Тестирование успешного входа
    @allure.title("Успешный логин стандартным пользователем")
    def test_success_login(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.login('standard_user', 'secret_sauce')
        assert "/inventory.html" in driver.current_url, "URL некорректный"
        assert login.is_inventory_page_loaded(), "Содержимое не загрузилось"
        driver.save_screenshot("success_login.png")
        with allure.step("Вход стандартным пользователем корректный"):
            allure.attach.file(
                "success_login.png",
                name="Успешный вход",
                attachment_type=allure.attachment_type.PNG
            )


    # Тестирование входа с неверным паролем
    @allure.title("Попытка входа с неверным паролем")
    def test_incorrect_password(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.login('standard_user', 'incorrect_password')
        assert driver.current_url == BASE_URL, "URL некорректный"
        assert login.get_text_error_message() == INCORRECT_PASSWORD_ERROR_MESSAGE,\
            "Сообщение об ошибке некорректно!"''
        driver.save_screenshot("incorrect_password.png")
        with allure.step("Сообщение об ошибке корректно"):
            allure.attach.file(
                "incorrect_password.png",
                name="Сообщение об ошибке",
                attachment_type=allure.attachment_type.PNG
            )


    # Тестирование входа заблокированным пользователем
    @allure.title("Попытка входа заблокированным пользователем")
    def test_locked_user(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.login('locked_out_user', 'secret_sauce')
        assert driver.current_url == BASE_URL, "URL некорректный"
        assert login.get_text_error_message() == LOCKED_USER_MESSAGE,\
            "Сообщение об ошибке некорректно!"
        driver.save_screenshot("locked_user.png")
        with allure.step("Сообщение об ошибке корректно"):
            allure.attach.file(
                "locked_user.png",
                name="Сообщение об ошибке",
                attachment_type=allure.attachment_type.PNG
            )


    # Тестирование входа с пустыми полями
    @allure.title("Попытка входа с пустыми полями")
    def test_empty_user(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.login('', '')
        assert driver.current_url == BASE_URL, "URL некорректный"
        assert login.get_text_error_message() == EMPTY_USER_MESSAGE, \
            "Сообщение об ошибке некорректно!"
        driver.save_screenshot("empty_user.png")
        with allure.step("Сообщение об ошибке корректно"):
            allure.attach.file(
                "empty_user.png",
                name="Сообщение об ошибке",
                attachment_type=allure.attachment_type.PNG
            )


    # Тестирование входа с задержками
    @allure.title("Попытка входа с задержками")
    def test_glitch_user(self, driver):
        login = LoginPage(driver)
        login.open(BASE_URL)
        login.login('performance_glitch_user', 'secret_sauce')
        assert "/inventory.html" in driver.current_url, "URL некорректный"
        assert login.is_inventory_page_loaded(), "Содержимое не загрузилось"
        driver.save_screenshot("glitch_user.png")
        with allure.step("Вход стандартным пользователем корректный"):
            allure.attach.file(
                "glitch_user.png",
                name="Сообщение об ошибке",
                attachment_type=allure.attachment_type.PNG
            )