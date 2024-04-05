import secrets
import string
from datetime import date

from pageObjects.AppointmentPage import AppointmentPage
from pageObjects.ConfirmationPage import ConfirmationPage
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        # create objects for the pages test interacts with
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        appointmentPage = AppointmentPage(self.driver)
        confirmationPage = ConfirmationPage(self.driver)

        # perform the tests below

        # click on Make Appointment link and get navigated to Login Page
        homePage.clickMakeAppointmentLink()
        print("Navigating to Login Page")

        # enter an incorrect username and password and login
        loginPage.enterUsernameField("somethingRandom")
        loginPage.enterPasswordField("junkjunkjunk")
        loginPage.clickLoginButton()

        # failed login message appears
        failedMessage = loginPage.getLoginMessage()
        assert "Login failed!" in failedMessage
        print("asserted message is correct")

        # enter a valid username and password and click on login
        loginPage.enterUsernameField("John Doe")
        loginPage.enterPasswordField("ThisIsNotAPassword")
        loginPage.clickLoginButton()

        # select a facility from the dropdown menu
        facility = "Hongkong CURA Healthcare Center"
        appointmentPage.getFacility(facility)

        # select checkbox `Apply for hospital readmission`
        appointmentPage.clickHospitalReadmission()

        # select `Medicaid` radio button
        appointmentPage.selectMedicaidProgram()

        # select today's date from calendar
        today = date.today()
        d1 = today.strftime("%d/%m/%Y") # dd/mm/YY
        print("Today's date =", d1)
        appointmentPage.enterDateField(d1)

        #  in any comment inside the `Comment` box
        randomComment = "This will be a random comment from me"
        appointmentPage.enterCommentField(randomComment)

        # select on `Book Appointment` button
        appointmentPage.clickBookAppointment()

        # confirm Appointment Confirmation text and the information and dates entered
        assert facility in confirmationPage.getFacilityConfirmation()
        print("validated", facility)
        assert "Yes" in confirmationPage.getReadmissionConfirmation()
        print("validated Yes for Readmission")
        assert "Medicaid" in confirmationPage.getHealthcareProgramConfirmation()
        print("validated Medicaid")
        assert d1 in confirmationPage.getVisitDateConfirmation()
        print("validated ", d1, " as date")
        assert randomComment in confirmationPage.getCommentConfirmation()
        print("validated '", randomComment, "' as the comment")

        # select on `Go to Homepage` button
        confirmationPage.clickGotoHomepageButton()

        # confirm navigation to homepage
        assert "https://katalon-demo-cura.herokuapp.com/" in appointmentPage.getCurrentUrl()

