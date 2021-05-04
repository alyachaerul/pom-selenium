import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time

import unittest
from Test_Data import TestData
from Locators import Locators
from Pages import HomePage

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=TestData.CHROME_PATH)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class IntegerTest(BaseTest):
    def test_001_addition(self):
        # Membuat objek HomePage
        self.homepage = HomePage(self.driver)

        # Input 1st number
        self.homepage.enter_text(Locators.INPUT_1, TestData.INTEGER_1)

        # Select Operator +
        self.homepage.select_operator(TestData.ADDITION_OP)

        # Input 2nd number
        self.homepage.enter_text(Locators.INPUT_2, TestData.INTEGER_2)

        # CLick equal sign
        self.homepage.click(Locators.EQUAL_BUTTON)

        # Ambil teks result
        result = self.homepage.get_text(Locators.RESULT)

        self.assertEqual("7", result)

    def test_002_substraction(self):
        # Membuat objek HomePage
        self.homepage = HomePage(self.driver)

        # Input 1st number
        self.homepage.enter_text(Locators.INPUT_1, TestData.INTEGER_1)

        # Select Operator +
        self.homepage.select_operator(TestData.SUBSTRACTION_OP)

        # Input 2nd number
        self.homepage.enter_text(Locators.INPUT_2, TestData.INTEGER_2)

        # CLick equal sign
        self.homepage.click(Locators.EQUAL_BUTTON)

        # Ambil teks result
        result = self.homepage.get_text(Locators.RESULT)

        self.assertEqual("1", result)

    def test_003_multiplication(self):
        # Membuat objek HomePage
        self.homepage = HomePage(self.driver)

        # Input angka ke kedua field lalu pilih operasi perkalian
        self.homepage.calculation(TestData.INTEGER_1, TestData.INTEGER_2, TestData.MULTIPLICATION_OP)

        # Ambil teks result
        result = self.homepage.get_text(Locators.RESULT)

        self.assertEqual("12", result)

    def test_004_division(self):
        # Membuat objek HomePage
        self.homepage = HomePage(self.driver)

        # Input angka ke kedua field lalu pilih operasi pembagian
        self.homepage.calculation(TestData.INTEGER_1, TestData.INTEGER_2, TestData.DIVISION_OP)

        # Ambil teks result
        result = self.homepage.get_text(Locators.RESULT)

        self.assertEqual("1.3333333333333333", result)