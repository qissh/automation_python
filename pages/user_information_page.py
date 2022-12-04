from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class User_information_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    first_name = '//*[@id="first-name"]'
    last_name = '//*[@id="last-name"]'
    postal_code = '//*[@id="postal-code"]'
    continue_button = '//*[@id="continue"]'

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions
    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('input first name ')


    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('input last name')

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print('input postal code')

    def click_continue_button(self):
        self.get_continue_button().click()
        print('click continue button')


    #methods
    def input_information(self):

        self.get_current_url()
        self.input_first_name('ivan')
        self.input_last_name('ivanov')
        self.input_postal_code('1111')
        self.click_continue_button()






