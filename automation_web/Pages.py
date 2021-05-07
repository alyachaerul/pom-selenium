from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random
import pytest

from TestData import TestData
from Locators import Locators

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    # Fungsi untuk mengeklik locator
    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)).click()

    # Fungsi untuk input/enter teks
    def enter_text(self, locator, teks):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)).send_keys(teks)

    # Fungsi untuk mengambil teks
    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)).text

    # Fungsi untuk mengecek elemen visible
    def is_visible(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return bool(element)
        except TimeoutException:
            return False
    
    # Fungsi untuk memilih item di dropdown
    def select_from_dropdown(self, locator, item):
        dropdown = Select(self.driver.find_element_by_id(locator))
        dropdown.select_by_visible_text(item)


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def signin(self):
        # Fungsi untuk klik tombol Sign In di Home Page
        self.click(Locators.SIGN_IN_BUTTON)
        self.is_visible(Locators.SIGN_IN_INPUT_EMAIL)

    def register_newsletter_valid(self):
        # Fungsi untuk daftar newsletter
        self.enter_text(Locators.NEWSLETTER_INPUT, TestData.NEWSLETTER_EMAIL)
        self.click(Locators.SUBMIT_NEWSLETTER)

    def register_newsletter_invalid(self):
        # Fungsi untuk daftar newsletter invalid
        self.enter_text(Locators.NEWSLETTER_INPUT, TestData.NEWSLETTER_INVALID_EMAIL)
        self.click(Locators.SUBMIT_NEWSLETTER)

    def contactus(self):
        # FUngsi untuk klik tombol COntact Us di Home Page
        self.click(Locators.CONTACT_US_BUTTON)
        self.is_visible(Locators.CONTACT_US_TEXT_AREA)


class AuthenticationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def signin_success(self):
        self.enter_text(Locators.SIGN_IN_INPUT_EMAIL, TestData.EMAIL)
        self.enter_text(Locators.SIGN_IN_INPUT_PASSWORD, TestData.PASSWORD)
        self.click(Locators.SIGN_IN_SUBMIT)
        self.is_visible(Locators.MY_ACCOUNT_PAGE_HEADER)
    
    def signin_email_invalid(self):
        # Step 1 - Input Email di field "Already registered"
        self.enter_text(Locators.SIGN_IN_INPUT_EMAIL, TestData.EMAIL_INVALID)

        # Step 2 - Input password 
        self.enter_text(Locators.SIGN_IN_INPUT_PASSWORD, TestData.PASSWORD)

        # Step 3 - Klik button SignIn
        self.click(Locators.SIGN_IN_SUBMIT)

        # Step 4 - Menunggu elemen muncul
        self.is_visible(Locators.INVALID_EMAIL_ALERT)

    def signin_password_invalid(self):
        # Step 1 - Input Email di field "Already Registered"
        self.enter_text(Locators.SIGN_IN_INPUT_EMAIL, TestData.EMAIL)

        # Step 2 - Input password 
        self.enter_text(Locators.SIGN_IN_INPUT_PASSWORD, TestData.PASSWORD_INVALID)

        # Step 3 - Klik button SignIn
        self.click(Locators.SIGN_IN_SUBMIT)

        # Step 4 - Menunggu elemen muncul
        self.is_visible(Locators.INVALID_PASSWORD_ALERT)
    
class ContactPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def send_message_to_cs(self):
        self.select_from_dropdown(Locators.CONTACT_US_DROPDOWN, TestData.DROPDOWN_CS)
        self.enter_text(Locators.CONTACT_US_EMAIL, TestData.CONTACT_EMAIL)
        self.enter_text(Locators.CONTACT_US_TEXT_AREA, TestData.CONTACT_MESSAGE)
        self.click(Locators.CONTACT_SEND)
        self.is_visible(Locators.CONTACT_ALERT)

