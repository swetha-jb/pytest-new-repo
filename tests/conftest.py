import pytest
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup(request):
    options = webdriver.ChromeOptions()
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # 🔑 navigate to login page before tests
    login_url = "https://accounts2.netgear.com/login?response_type=code&client_id=...&scope=...&redirect_uri=..."
    driver.get(login_url)

    request.cls.driver = driver
    yield driver
    driver.quit()

