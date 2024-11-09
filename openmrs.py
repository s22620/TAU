from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class OpenMRSTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 3)

    def test_add_and_delete_patient(self):
        driver = self.driver
        driver.get("https://demo.openmrs.org/openmrs/login.htm")

        # Logowanie
        username_input = self.wait.until(EC.visibility_of_element_located((By.ID, "username")))
        password_input = driver.find_element(By.ID, "password")
        location_selection = driver.find_element(By.ID, "Inpatient Ward")
        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, "loginButton")))

        username_input.send_keys("admin")
        password_input.send_keys("Admin123")
        location_selection.click()
        login_button.click()

        # Przejście do zakładki "Register a Patient"
        register_patient_button = self.wait.until(EC.element_to_be_clickable((By.ID, "referenceapplication-registrationapp-registerPatient-homepageLink-referenceapplication-registrationapp-registerPatient-homepageLink-extension")))
        register_patient_button.click()

        # Wprowadzenie danych pacjenta
        given_name_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "givenName")))
        given_name_input.send_keys("Test")

        family_name_input = driver.find_element(By.NAME, "familyName")
        family_name_input.send_keys("Patient")

        # Kliknij przycisk "Next"
        driver.find_element(By.ID, "next-button").click()

        # Wprowadź płeć
        gender_input = self.wait.until(EC.visibility_of_element_located((By.ID, "gender-field")))
        gender_input.send_keys("Male")
        driver.find_element(By.ID, "next-button").click()

        # Wprowadź datę urodzenia
        birthdate_day = self.wait.until(EC.visibility_of_element_located((By.ID, "birthdateDay-field")))
        birthdate_day.send_keys("01")

        birthdate_month = driver.find_element(By.ID, "birthdateMonth-field")
        birthdate_month.send_keys("January")

        birthdate_year = driver.find_element(By.ID, "birthdateYear-field")
        birthdate_year.send_keys("1990")
        driver.find_element(By.ID, "next-button").click()

        # Wprowadź adres
        address_input = self.wait.until(EC.visibility_of_element_located((By.ID, "address1")))
        address_input.send_keys("123 Main Street")
        driver.find_element(By.ID, "next-button").click()

        # Wprowadź numer telefonu
        phone_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "phoneNumber")))
        phone_input.send_keys("123456789")
        driver.find_element(By.ID, "next-button").click()


    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
