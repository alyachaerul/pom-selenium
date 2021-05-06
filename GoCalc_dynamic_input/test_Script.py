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
from Test_Data import TestData
from Locators import Locators
from Pages import HomePage

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

    def test_001_addition_dynamic(self):
        # Membuat objek HomePage
        self.homepage = HomePage(self.driver)

        # Input angka ke kedua field lalu pilih operasi penjumlahan
        hasil = self.homepage.calculation_dynamic_integer(TestData.ADDITION_OP)

        # Ambil teks result
        result = self.homepage.get_text(Locators.RESULT)

        self.assertEqual(str(hasil), result)

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

    def test_002_substraction_dynamic(self):
        # Membuat objek HomePage
        self.homepage = HomePage(self.driver)

        # Input angka ke kedua field lalu pilih operasi pengurangan
        hasil = self.homepage.calculation_dynamic_integer(TestData.SUBSTRACTION_OP)

        # Ambil teks result
        result = self.homepage.get_text(Locators.RESULT)

        self.assertEqual(str(hasil), result)

    def test_003_multiplication(self):
        # Membuat objek HomePage
        self.homepage = HomePage(self.driver)

        # Input angka ke kedua field lalu pilih operasi perkalian
        self.homepage.calculation(TestData.INTEGER_1, TestData.INTEGER_2, TestData.MULTIPLICATION_OP)

        # Ambil teks result
        result = self.homepage.get_text(Locators.RESULT)

        self.assertEqual("12", result)

    def test_003_multiplication_dynamic(self):
        # Membuat objek HomePage
        self.homepage = HomePage(self.driver)

        # Input angka ke kedua field lalu pilih operasi perkalian
        hasil = self.homepage.calculation_dynamic_integer(TestData.MULTIPLICATION_OP)

        # Ambil teks result
        result = self.homepage.get_text(Locators.RESULT)

        self.assertEqual(str(hasil), result)

    def test_004_division(self):
        # Membuat objek HomePage
        self.homepage = HomePage(self.driver)

        # Input angka ke kedua field lalu pilih operasi pembagian
        self.homepage.calculation(TestData.INTEGER_1, TestData.INTEGER_2, TestData.DIVISION_OP)

        # Ambil teks result
        result = self.homepage.get_text(Locators.RESULT)

        self.assertEqual("1.3333333333333333", result)

    def test_004_division_dynamic(self):
        # Membuat objek HomePage
        self.homepage = HomePage(self.driver)

        # Input angka ke kedua field lalu pilih operasi pembagian
        hasil = self.homepage.calculation_dynamic_integer(TestData.DIVISION_OP)

        # Ambil teks result
        result = self.homepage.get_text(Locators.RESULT)

        self.assertEqual(str(hasil), result)


class DecimalTest(BaseTest):
    def test_001_addition(self):
        # Membuat objek HomePage
        self.homepage = HomePage(self.driver)

        # Input angka ke kedua field lalu pilih operasi penjumlahan
        self.homepage.calculation(TestData.DECIMAL_1, TestData.DECIMAL_2, TestData.ADDITION_OP)

        # Ambil teks result
        result = self.homepage.get_text(Locators.RESULT)

        self.assertEqual("3", result)


    def test_002_substraction(self):
        # Membuat objek HomePage
        self.homepage = HomePage(self.driver)

        # Input angka ke kedua field lalu pilih operasi pengurangan
        self.homepage.calculation(TestData.DECIMAL_1, TestData.DECIMAL_2, TestData.SUBSTRACTION_OP)

        # Ambil teks result
        result = self.homepage.get_text(Locators.RESULT)

        self.assertEqual("1.8", result)

    def test_003_multiplication(self):
        # Membuat objek HomePage
        self.homepage = HomePage(self.driver)

        # Input angka ke kedua field lalu pilih operasi perkalian
        self.homepage.calculation(TestData.DECIMAL_1, TestData.DECIMAL_2, TestData.MULTIPLICATION_OP)

        # Ambil teks result
        result = self.homepage.get_text(Locators.RESULT)

        self.assertEqual("1.44", result)

    def test_004_division(self):
        # Membuat objek HomePage
        self.homepage = HomePage(self.driver)

        # Input angka ke kedua field lalu pilih operasi pembagian
        self.homepage.calculation(TestData.DECIMAL_1, TestData.DECIMAL_2, TestData.DIVISION_OP)

        # Ambil teks result
        result = self.homepage.get_text(Locators.RESULT)

        self.assertEqual("4", result)


class ErrorTest(BaseTest):
    def test_001_input_empty(self):
        # Membuat objek HomePage
        self.homepage = HomePage(self.driver)

        # Select Operator *
        self.homepage.select_operator(TestData.ADDITION_OP)

        # Input 2nd number
        self.homepage.enter_text(Locators.INPUT_2, TestData.INTEGER_2)

        # CLick equal sign
        self.homepage.click(Locators.EQUAL_BUTTON)

        actual_text = self.homepage.get_text(Locators.RESULT)

        self.assertEqual("Error: Input value cannot be empty!", actual_text)