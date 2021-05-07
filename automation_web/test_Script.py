import datetime
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time

import unittest
from TestData import TestData
from Locators import Locators
from Pages import HomePage, AuthenticationPage, ContactPage

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=TestData.CHROME_PATH)
        self.driver.maximize_window()

    def tearDown(self):
        # Take a Screen-shot of the drive homepage, when a test case is failed or an error raised.
        for method, error in self._outcome.errors:
            if error:
                date_stamp = str(datetime.datetime.now()).split('.')[0]
                date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
                name = "screenshot" + self.id() + date_stamp + ".png"
                self.driver.get_screenshot_as_file(name)
                print(name)

        self.driver.close()
        self.driver.quit()

class ContactUsTest(BaseTest):
    def test_send_message_to_cs(self):
        # Membuat objek homepage
        self.homepage = HomePage(self.driver)

        # Klik tombol contact us
        self.homepage.contactus()

        # Membuat objek contact page
        self.contactpage = ContactPage(self.homepage.driver)

        # Kirim pesan ke CS
        self.contactpage.send_message_to_cs()

        # Assertion
        success_text = self.contactpage.get_text(Locators.CONTACT_ALERT)
        self.assertEqual(success_text, TestData.CONTACT_SUCCESS_ALERT)

class LoginTest(BaseTest):
    def test_login_success(self):
        # Membuat objek Home Page
        self.homepage = HomePage(self.driver)

        # Klik tombol sign in
        self.homepage.signin()

        # Membuat objek Authentiaction Page
        self.authenticationpage = AuthenticationPage(self.homepage.driver)

        # Isi email dan password dan klik tombol Sign In
        self.authenticationpage.signin_success()

        # Assertion
        header = self.authenticationpage.get_text(Locators.MY_ACCOUNT_PAGE_HEADER)
        self.assertEqual("MY ACCOUNT", header)

    def test_login_failed(self):
        # Membuat objek homepage
        self.homepage = HomePage(self.driver)

        # Klik tombol sign in
        self.homepage.signin()

        # Membuat objek authentication page
        self.authenticationpage = AuthenticationPage(self.homepage.driver)

        # Panggil fungsi signin dengan email invalid
        self.authenticationpage.signin_email_invalid()

        # Assertion
        failed_email_result = self.homepage.get_text(Locators.INVALID_EMAIL_ALERT)

        self.assertEqual(failed_email_result, TestData.ALERT_EMAIL_INVALID)
    
    def test_login_password_invalid(self):
        # Membuat objek homepage
        self.homepage = HomePage(self.driver)

        # Klik tombol sign in
        self.homepage.signin()

        # Membuat objek authentication page
        self.authenticationpage = AuthenticationPage(self.homepage.driver)

        # Panggil fungsi signin dengan password invalid
        self.authenticationpage.signin_password_invalid()

        # Assertion
        failed_password_result = self.homepage.get_text(Locators.INVALID_PASSWORD_ALERT)

        self.assertEqual(failed_password_result, TestData.ALERT_PASSWORD_INVALID)
    
    def test_both_field_empty(self):
        # Membuat objek homepage
        self.homepage = HomePage(self.driver)

        # Klik tombol sign in
        self.homepage.signin()

        # Membuat objek authentication page
        self.authenticationpage = AuthenticationPage(self.homepage.driver)

        self.homepage.click(Locators.SIGN_IN_SUBMIT)

        # Assertion
        empty_field_result = self.homepage.get_text(Locators.EMAIL_REQUIRED_ALERT)
        self.assertEqual(empty_field_result, TestData.ALERT_EMAIL_REQUIRED)

class NewsletterTest(BaseTest):

    def test_register_newsletter_valid(self):
        # Step 1 - Membuat objek Home Page
        self.homepage = HomePage(self.driver)

        # Step 2 - Masukkan email di Newletter
        self.homepage.enter_text(Locators.NEWSLETTER_INPUT, TestData.NEWSLETTER_EMAIL)
        print(TestData.NEWSLETTER_EMAIL)
        # Step 3 - Click Submit button
        self.homepage.click(Locators.SUBMIT_NEWSLETTER)

        # # Step 2 & 3 - Masukkan email dan Click Submit
        # self.homepage.register_newsletter_valid()

        # Assertion
        teks = self.homepage.get_text(Locators.NEWSLETTER_ALERT)
        self.assertEqual(TestData.NEWSLETTER_SUCCESS, teks)

    def test_register_newsletter_invalid(self):
        pass

    def test_register_newsletter_registered(self):
        pass