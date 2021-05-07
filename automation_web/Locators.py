from selenium.webdriver.common.by import By
import pytest

class Locators():
    # -- Home Page Locators --
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "a.login")
    CONTACT_US_BUTTON = (By.ID, "contact-link")
    NEWSLETTER_INPUT = (By.ID, "newsletter-input")
    SUBMIT_NEWSLETTER = (By.NAME, "submitNewsletter")
    NEWSLETTER_ALERT = (By.CSS_SELECTOR, "p.alert")
    NEWSLETTER_ALERT_DANGER = (By.CSS_SELECTOR, "p.alert.alert-danger")
    NEWSLETTER_ALERT_SUCCESS = (By.CSS_SELECTOR, "p.alert.alert-success")

    # -- Authentication Page Locators --
    SIGN_IN_INPUT_EMAIL = (By.ID, "email")
    SIGN_IN_INPUT_PASSWORD = (By.ID, "passwd")
    SIGN_IN_SUBMIT = (By.ID, "SubmitLogin")
    INVALID_EMAIL_ALERT = (By.XPATH, "//*[contains(text(), 'Invalid email address.')]")
    INVALID_PASSWORD_ALERT = (By.XPATH, "//*[@id='center_column']/div[1]/ol/li")
    EMAIL_REQUIRED_ALERT = (By.XPATH, "//*[@id='center_column']/div[1]/ol/li")

    # -- My Account Page Locators --
    MY_ACCOUNT_PAGE_HEADER = (By.CSS_SELECTOR, "h1.page-heading")

    # -- Contact Us -- 
    CONTACT_US_TEXT_AREA = (By.ID, "message")
    CONTACT_US_DROPDOWN = "id_contact"
    CONTACT_US_EMAIL = (By.ID, "email")
    CONTACT_ALERT = (By.CSS_SELECTOR, "p.alert")
    CONTACT_SEND = (By.ID, "submitMessage")