import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page
from pages.user_information_page import User_information_page


def test_link_aabout():


    driver = webdriver.Chrome(executable_path='//Users//georgijsemenov//PycharmProjects//selenium//chromedriver')
    print('start test')

    login = Login_page(driver)
    login.autorisation()

    mp = Main_page(driver)
    mp.select_menu_about()



    time.sleep(5)
    driver.quit()

