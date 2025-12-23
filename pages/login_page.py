from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # Локаторы
    USERNAME_LOCATOR = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD_LOCATOR = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//*[@id="login-button"]')
    INVENTORY_CONTAINER_LOCATOR = (By.ID, "inventory_container")
    ERROR_MESSAGE_LOCATOR = (
        By.XPATH,
        '//*[@id="login_button_container"]/div/form/div[3]'
    )

    # Конструктор
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Функция открытия страницы
    def open(self, url):
        self.driver.get(url)

    # Функция авторизация
    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_LOCATOR).send_keys(username)
        self.driver.find_element(*self.PASSWORD_LOCATOR).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR).click()

    # Проверка загрузки элементов страницы
    def is_inventory_page_loaded(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.INVENTORY_CONTAINER_LOCATOR)
            ).is_displayed()

    # Получить текст сообщения об ошибке
    def get_text_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE_LOCATOR)
        ).text