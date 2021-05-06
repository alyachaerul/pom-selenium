import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from Test_Data import TestData
from Locators import Locators
import unittest


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

    # Fungsi untuk memilih operator
    def select_operator(self,operators):
        operator = Select(self.driver.find_element_by_id("op"))
        operator.select_by_visible_text(operators)

    # Fungsi untuk mengambil teks
    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)).text


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def calculation(self, number_1, number_2, operator):
        self.enter_text(Locators.INPUT_1, number_1)
        self.select_operator(operator)
        self.enter_text(Locators.INPUT_2, number_2)
        self.click(Locators.EQUAL_BUTTON)
