import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # run in headless mode (no UI)
    options.add_argument("--no-sandbox")  # required inside docker
    options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--remote-debugging-port=9222")  # avoid user-data-dir conflicts

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

