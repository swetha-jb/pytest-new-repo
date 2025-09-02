import time

import pytest
from selenium import webdriver


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://accounts2.netgear.com/login?redirectUrl=https:%2F%2Finsight.netgear.com%2F&clientId=6dlf5ppqm5oic7hhtk68qrlc9j")
    time.sleep(3)
    request.cls.driver = driver
    yield
    driver.quit()




