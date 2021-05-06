import pytest
from selenium.webdriver.common.by import By

class Locators():
    INPUT_1 = (By.ID, 'numberA') 
    INPUT_2 = (By.ID, 'numberB') 
    EQUAL_BUTTON = (By.CSS_SELECTOR, 'input[type=button]')
    RESULT = (By.ID, "result")
    