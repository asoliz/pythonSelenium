from selenium.webdriver.common.by import By

from pageObjects.AppointmentPage import AppointmentPage
from pageObjects.LoginPage import LoginPage


class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    # declare all the objects on the Login page

    # Confirmation header
    confirmationHeader = (By.XPATH, "//h2[normalize-space()='Appointment Confirmation']")
    # confirmation message
    confirmationMessage = (By.XPATH, "//p[@class='lead']")
    # facility result
    facilityText = (By.ID, "facility")
    # hospital liason
    readmissionFlag = (By.ID, "hospital_readmission")
    # healthcare program result
    healthcareProgram = (By.ID, "program")
    # visit date
    visitDate = (By.ID, "visit_date")
    # comment text
    commentText = (By.XPATH, "//p[@id='comment']")
    # goto homepage link
    gotoHomepageLink = (By.LINK_TEXT, "Go to Homepage")

    # declare all common functions

    # getting confirmation header
    def getConfirmationHeader(self):
        return self.driver.find_element(*ConfirmationPage.confirmationHeader).text

    # get confirmation message
    def getConfirmationMessage(self):
        return self.driver.find_element(*ConfirmationPage.confirmationMessage).text

    # get confirmation on facility
    def getFacilityConfirmation(self):
        return self.driver.find_element(*ConfirmationPage.facilityText).text

    # get confirmation on readmission
    def getReadmissionConfirmation(self):
        return self.driver.find_element(*ConfirmationPage.readmissionFlag).text

    # get confirmation on Heatlhcare Program
    def getHealthcareProgramConfirmation(self):
        return self.driver.find_element(*ConfirmationPage.healthcareProgram).text

    # get confirmation on Visit Date
    def getVisitDateConfirmation(self):
        return self.driver.find_element(*ConfirmationPage.visitDate).text

    # get confirmation on Comment
    def getCommentConfirmation(self):
        return self.driver.find_element(*ConfirmationPage.commentText).text

    # click Go To Homepage
    def clickGotoHomepageButton(self):
        self.driver.find_element(*ConfirmationPage.gotoHomepageLink).click()
        appointmentPage = AppointmentPage(self.driver)
        return appointmentPage
