import time

import pytest
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

@pytest.mark.run(order=3)
def test_buy_products_1():


    driver = webdriver.Chrome(executable_path='//Users//georgijsemenov//PycharmProjects//selenium//chromedriver')
    print('start test 1')

    login = Login_page(driver)
    login.autorisation()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    uip = User_information_page(driver)
    uip.input_information()

    p = Payment_page(driver)
    p.click_finish_button()

    f = Finish_page(driver)
    f.finish()

    time.sleep(5)


@pytest.mark.run(order=1)
def test_buy_products_2():


    driver = webdriver.Chrome(executable_path='//Users//georgijsemenov//PycharmProjects//selenium//chromedriver')
    print('start test 2')

    login = Login_page(driver)
    login.autorisation()

    mp = Main_page(driver)
    mp.select_products_2()

    cp = Cart_page(driver)
    cp.click_checkout_button()
    time.sleep(5)

@pytest.mark.run(order=2)
def test_buy_products_3():


    driver = webdriver.Chrome(executable_path='//Users//georgijsemenov//PycharmProjects//selenium//chromedriver')
    print('start test 3')

    login = Login_page(driver)
    login.autorisation()

    mp = Main_page(driver)
    mp.select_products_3()

    cp = Cart_page(driver)
    cp.click_checkout_button()
    time.sleep(5)