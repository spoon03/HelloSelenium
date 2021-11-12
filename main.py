"""Тут мы пишем тесты"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from main_page import MainPage


driver = webdriver.Chrome(ChromeDriverManager().install())
main_page = MainPage(driver)
main_page.open()
assert "Яндекс" in driver.title
main_page.seacrh("Python")
main_page.wait_result()
assert "Python" in main_page.page_source()
main_page.quit()
