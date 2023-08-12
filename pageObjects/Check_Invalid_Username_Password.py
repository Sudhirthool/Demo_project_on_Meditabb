from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class Meditab_Invalid_data:
    Text_Clinic_XPATH = (By.XPATH, "//mtab-input-text[@id='clinic']//input[@type='TEXT']")
    Text_Username_XPATH =(By.XPATH, "//mtab-input-text[@id='username']//input[@type='TEXT']")
    Text_Password_CSS =(By.CSS_SELECTOR, "input[type='PASSWORD']")
    Click_Login_Button_XPATH = (By.XPATH, "//span[@class='ui-button-text ui-clickable']")
    Alert_Invalid_Data_XPATH = (By.XPATH, "//span[@class='mtab-login-error-message']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=0.5)

    def Enter_Clinic(self, clinic):
        self.driver.find_element(*Meditab_Invalid_data.Text_Clinic_XPATH).send_keys(clinic)

    def Enter_Username(self, username):
        self.driver.find_element(*Meditab_Invalid_data.Text_Username_XPATH).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(*Meditab_Invalid_data.Text_Password_CSS).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(*Meditab_Invalid_data.Click_Login_Button_XPATH).click()

    def verify_Invalid_MSG(self):

        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.Alert_Invalid_Data_XPATH))
            self.driver.find_element(*Meditab_Invalid_data.Alert_Invalid_Data_XPATH)
            print(self.driver.find_element(*Meditab_Invalid_data.Alert_Invalid_Data_XPATH).text)
            return True
        except:
            return False









