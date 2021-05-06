from faker import Faker
import pytest

class TestData():
    faker = Faker()
    # -- Driver
    CHROME_PATH = r"/Users/rayhanalya/Documents/BinarFSW/BinarQA/chromedriver"

    # -- URL
    BASE_URL = "http://automationpractice.com/index.php?"

    # Login
    EMAIL = "extract1234@yopmail.com"
    PASSWORD = "1qwerty"
    EMAIL_INVALID = "extract@yopmail"
    PASSWORD_INVALID = "qwertyui"
    ALERT_EMAIL_INVALID = "Invalid email address."
    ALERT_PASSWORD_INVALID = "Authentication failed."
    ALERT_EMAIL_REQUIRED = "An email address required."

    # -- Email Newsletter
    NEWSLETTER_EMAIL = faker.ascii_email()
    NEWSLETTER_INVALID_EMAIL = "extract1234@"

    # -- Alert Newsletter
    NEWSLETTER_SUCCESS = "Newsletter : You have successfully subscribed to this newsletter."
    NEWSLETTER_INVALID = "Newsletter : Invalid email address."
    NEWSLETTER_REGISTERED = "Newsletter : This email address is already registered."

    # Contact Us
    DROPDOWN_CS = "Customer Service"
    DROPDOWN_WM = "Webmaster"
    CONTACT_EMAIL = faker.ascii_email()
    CONTACT_MESSAGE = "Lorem ipsum dolor sit amet...."
    CONTACT_SUCCESS_ALERT = "Your message has been successfully sent to our team."
