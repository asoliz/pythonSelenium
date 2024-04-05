import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# below we will declare a runtime variable called `browser` in order to pass which browser to run tests on (chrome, firefox, edge, etc)

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("browser")  # stores the value from the command-line

    # write conditional for what to do based on browser input
    if browser == "chrome":
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj)

    elif browser == "firefox":
        service_obj = Service()
        driver = webdriver.Firefox(service=service_obj)

    elif browser == "edge":
        service_obj = Service()
        driver = webdriver.Edge(service=service_obj)

    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # consider any client side mods below:
    # driver.maximize_window()
    request.cls.driver = driver  # sends `driver` to class object

    yield  # this means all test cases will run and then return to perform the following code
    driver.close()
