# Gerekli kütüphaneleri içe aktar
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from constants.magicStringDenemeleri import *
import pytest


# Test fonksiyonu
def test_saucedemo_login():
    # WebDriver konfigürasyonu
    driver = webdriver.Chrome()

    # SauceDemo'ya giriş yapmak için kullanıcı adı ve şifre
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'

    # SauceDemo web sitesini aç
    driver.get('https://www.saucedemo.com')

    # Kullanıcı adı ve şifre ile giriş yap
    sleep(3)
    driver.find_element(By.ID,username_id).send_keys(USERNAME)
    driver.find_element(By.ID,password_id).send_keys(PASSWORD)
    driver.find_element(By.ID,login_button_id).click()

    # İlk ürünü sepete ekle
    sleep(3)
    driver.find_element(By.ID,addCart_id).click()

    # Sepet sayfasına git
    sleep(3)
    driver.find_element(By.CLASS_NAME,shoppingCart_id).click()

    # Sepetin içindeki ürünleri doğrula
    sleep(3)
    assert 'Sauce Labs Backpack' in driver.page_source


# Pytest ile testi çalıştırmak için terminalde aşağıdaki komutu kullanabilirsiniz:
# pytest test_saucedemo.py
    
def test_sauce_demo():
    # WebDriver konfigürasyonu
    driver = webdriver.Chrome()

    # SauceDemo'ya giriş yapmak için kullanıcı adı ve şifre
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'

    # SauceDemo web sitesini aç
    driver.get('https://www.saucedemo.com')

    # Kullanıcı adı ve şifre ile giriş yap
    driver.find_element(By.ID,username_id).send_keys(USERNAME)
    driver.find_element(By.ID,password_id).send_keys(PASSWORD)
    driver.find_element(By.ID,login_button_id).click()

    # İlk ürünü sepete ekle
    driver.find_element(By.ID,addCart_id).click()

    # Sepet sayfasına git
    driver.find_element(By.CLASS_NAME,shoppingCart_id).click()
    sleep(3)
    # Sepetten ürünü çıkar
    driver.find_element(By.ID,remove_id).click()
    sleep(3)
    # Sepetin boş olduğunu doğrula
    assert 'Sauce Labs Backpack' not in driver.page_source

# Test fonksiyonu
@pytest.fixture
def browser():
    # WebDriver konfigürasyonu
    driver = webdriver.Chrome()
    yield driver
    # Testi bitir ve tarayıcıyı kapat
    driver.quit()

def test_checkout_complete(browser):
    # SauceDemo'ya giriş yapmak için kullanıcı adı ve şifre
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'

    # SauceDemo web sitesini aç
    browser.get('https://www.saucedemo.com')
    sleep(3)

    # Kullanıcı adı ve şifre ile giriş yap
    browser.find_element(By.ID,username_id).send_keys(USERNAME)
    browser.find_element(By.ID,password_id).send_keys(PASSWORD)
    browser.find_element(By.ID,login_button_id).click()
    sleep(3)

    # İlk ürünü sepete ekle
    browser.find_element(By.ID,addCart_id).click()
    sleep(3)

    # Checkout sayfasına git
    browser.find_element(By.CLASS_NAME,shoppingCart_id).click()
    browser.find_element(By.ID,checkout_id).click()
    sleep(3)

    # Checkout bilgilerini gir
    browser.find_element(By.ID,firstName_id).send_keys('Test')
    browser.find_element(By.ID,lastName_id).send_keys('User')
    browser.find_element(By.ID,postalCode_id).send_keys('12345')
    browser.find_element(By.ID,continue_id).click()
    sleep(3)

    # Checkout işlemini tamamla
    browser.find_element(By.ID,finish_id ).click()
    sleep(3)
    # Checkout işleminin tamamlandığını doğrula
    assert checkout_text in browser.page_source

# Pytest ile testi çalıştırmak için terminalde aşağıdaki komutu kullanabilirsiniz:
# pytest test_checkout.py



