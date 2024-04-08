from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AppointmentPage:
    def __init__(self, driver):
        self.driver = driver

    # declare all the objects on the Login page

    # facility drop down menu
    facilityDropdown = (By.ID, "combo_facility")
    # apply for hospital readmission checkbox
    readmissionCheck = (By.CSS_SELECTOR, ".checkbox-inline")
    # healthcare program selections
    medicaidProgram = (By.ID, "radio_program_medicaid")
    medicareProgram = (By.ID, "radio_program_medicare")
    noProgram = (By.ID, "radio_program_none")
    # visit date calendar
    dateField = (By.ID, "txt_visit_date")
    # comment section
    commentField = (By.ID, "txt_comment")
    # Book appointment button
    bookAppointment = (By.XPATH, "//button[@id='btn-book-appointment']")


    # select the Facility
    def defGetFacilityDropdown(self):
        return self.driver.find_element(*AppointmentPage.facilityDropdown)

    # click hospital readmission checkbox
    def clickHospitalReadmission(self):
        return self.driver.find_element(*AppointmentPage.readmissionCheck).click()

    # click
    def selectMedicaidProgram(self):
        return self.driver.find_element(*AppointmentPage.medicaidProgram).click()

    def selectMedicareProgram(self):
        return self.driver.find_element(*AppointmentPage.medicareProgram).click()

    def selectNoProgram(self):
        return self.driver.find_element(*AppointmentPage.noProgram).click()

    def enterDateField(self, text):
        return self.driver.find_element(*AppointmentPage.dateField).send_keys(text)

    def enterCommentField(self, text):
        return self.driver.find_element(*AppointmentPage.commentField).send_keys(text)

    def clickBookAppointment(self):
        return self.driver.find_element(*AppointmentPage.bookAppointment).click()

