"""Описание основной таблицы."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:
    """Класс с описанием основной страницы."""

    def __init__(self, driver) -> None:
        """
        Инициализация.

        :param driver:получаем вебдрайвер
        """
        self.driver = driver
        self.url = "https://ya.ru/"

    def _search_input(self) -> None:
        """
        Ищем строку ввода для поиска.
        :return:
        """
        return self.driver.find_element(By.ID, "text")

    def open(self) -> None:
        """Открытие страницы."""
        self.driver.get(self.url)

    def seacrh(self, item: str) -> None:
        """Вводим текст и ищем."""
        self._search_input().clear()
        self._search_input().send_keys(item)
        self.driver.find_element(By.CLASS_NAME, 'search2__button').click()

    def quit(self) -> None:
        """Закрываем драйвер."""
        self.driver.quit()

    def page_source(self) -> str:
        """Возвращаем DOM."""
        return self.driver.page_source

    def wait_result(self) -> None:
        """Ожидаем открытия страницы с результатом поиска."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'service__name')))
