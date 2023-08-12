import allure

from pageObjects.Check_Invalid_Username_Password import Meditab_Invalid_data
from utilities.Logger import LogGenerator
from utilities.ReadConfig import Readconfig
from allure_commons.types import AttachmentType

class Test_Meditab_Invalid_Credentials:
    Clinic = Readconfig.GetClinic()
    Username = Readconfig.GetUserName()
    Password = Readconfig.GetPassword()
    log = LogGenerator.loggen()

    def test_invalid_credentials(self, setup):

        self.log.info("Testcase test_invalid_credentials started")
        self.log.info("Opening Browser")
        self.driver = setup
        self.lp = Meditab_Invalid_data(self.driver)
        self.log.info("Entering Clinic"+self.Clinic)
        self.lp.Enter_Clinic(self.Clinic)
        self.log.info("Entering Username"+self.Username)
        self.lp.Enter_Username(self.Username)
        self.log.info("Entering Password"+self.Password)
        self.lp.Enter_Password(self.Password)
        self.log.info("Clicking Login Button")
        self.lp.Click_Login()

        if self.lp.verify_Invalid_MSG() == True:
            self.log.info("taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_invalid_credentials_pass", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("D:\\sudhir\\software testing\\Automation Pytest Selenium Practice\\pythonProject\\Screenshots\\test_invalid_pass.png")
            self.log.info("TestCase test_invalid_credentials Passed")
            assert True

        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_invalid_credentials fail",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(
                "D:\\sudhir\\software testing\\Automation Pytest Selenium Practice\\pythonProject\\Screenshots\\test_invalid_fail.png")
            self.log.info("TestCase test_invalid_credentials Failed")
            assert False




