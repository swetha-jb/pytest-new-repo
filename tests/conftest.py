import pytest
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup(request):
    options = webdriver.ChromeOptions()

    # give Chrome a unique profile each run (avoids user-data-dir conflicts)
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    options.add_argument("--headless")  # run in headless mode (no UI)
    options.add_argument("--no-sandbox")  # required inside docker
    options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    # 🔑 Navigate directly to your login URL
    login_url = (
        "https://accounts2.netgear.com/login"
        "?response_type=code"
        "&client_id=YOUR_CLIENT_ID"
        "&scope=openid%20email%20profile"
        "&redirect_uri=https://example.com/callback"
    )
    driver.get(login_url)

    request.cls.driver = driver
    yield driver
    driver.quit()

