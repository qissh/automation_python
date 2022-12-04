from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    select_product_1 = '//*[@id="add-to-cart-sauce-labs-backpack"]'
    select_product_2 = '//*[@id="add-to-cart-sauce-labs-bike-light"]'
    select_product_3 = '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'
    cart = '//*[@id="shopping_cart_container"]/a'
    menu = '//*[@id="react-burger-menu-btn"]'
    link_about = '//*[@id="about_sidebar_link"]'


    # Getters
    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))
    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))
    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_link_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))



    # Actions
    def click_select_product_1(self):
        self.get_select_product_1().click()
        print('click product 1 ')

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print('click product 2 ')

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print('click product 3 ')

    def click_cart(self):
        self.get_cart().click()
        print('click cart ')

    def click_menu(self):
        self.get_menu().click()
        print('click menu ')

    def click_link_about(self):
        self.get_link_about().click()
        print('click link about ')




    #methods
    def select_products_1(self):

        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_products_2(self):

        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_products_3(self):

        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()

    def select_menu_about(self):

        self.get_current_url()
        self.click_menu()
        self.click_link_about()
        self.asser_url('https://saucelabs.com/')



