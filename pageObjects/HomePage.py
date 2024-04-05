from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # declare all the objects on the Login page
    # top-right hamburger menu
    menuLink = (By.ID, "menu-toggle")
    # main `make appointment` button
    makeAppointmentLink = (By.ID, "btn-make-appointment")

    # declare all the functions in order to access them in other tests

    # click the menu link
    def clickMenuLink(self):
        return self.driver.find_element(*HomePage.menuLink)

    # click main Make Appointment link
    def clickMakeAppointmentLink(self):
        self.driver.find_element(*HomePage.makeAppointmentLink).click()
        loginPage = LoginPage(self.driver)
        return loginPage
