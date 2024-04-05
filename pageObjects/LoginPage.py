from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.AppointmentPage import AppointmentPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # declare all the objects on the Login page
    # username field
    usernameField = (By.ID, "txt-username")
    # password field
    passwordField = (By.XPATH, "//input[@id='txt-password']")
    # login button
    loginButton = (By.ID, "btn-login")
    # failed login message
    failedLoginMessage = (By.XPATH, "//p[@class='lead text-danger']")

    # declare all the functions in order to access them in other tests
    # enter username
    def enterUsernameField(self, text):
        return self.driver.find_element(*LoginPage.usernameField).send_keys(text)

    # enter password
    def enterPasswordField(self, text):
        return self.driver.find_element(*LoginPage.passwordField).send_keys(text)

    # click loginButton
    def clickLoginButton(self):
        self.driver.find_element(*LoginPage.loginButton).click()
        appointmentPage = AppointmentPage(self.driver)
        return appointmentPage

    # get failed login message
    def getLoginMessage(self):
        # wait = WebDriverWait(self.driver, 10)  # waiting sometime for page to load element
        # wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//p[@class='lead text-danger']")))
        return self.driver.find_element(*LoginPage.failedLoginMessage).text
