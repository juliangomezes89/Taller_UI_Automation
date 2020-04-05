import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.select import Select


class BookingTest(unittest.TestCase):
    # Este método se ejecuta la primera vez para instanciar el navegador
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="ui_testing/drivers/chromedriver.exe")
        cls.driver.maximize_window()

    # Este método recibe como parámetro la URL del sitio
    def test_go_url(self, url):
        self.driver.get(url)
    # Este método recibe como parámetro el login y password y hace clic en el botin Sign - In
    def test_login(self, user, password):
        self.driver.find_element_by_name("userName").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("login").click()
    # Este método hace clic en el botón SIGN-OFF
    def test_logout(self):
        self.driver.find_element_by_link_text("SIGN-OFF")
        time.sleep(2)
    def test_image(self):
        image = self.driver.find_element_by_xpath("//img[contains(@src,'mast_flightfinder.gif')]").is_displayed()
        self.assertTrue(image)

    def test_filters(self, tripType, passCount, fromPort, fromMonth, fromDay, toPort, toMonth, toDay, servClass):
        self.driver.find_element_by_xpath("//input[@name='tripType' and @value='"+tripType+"']").click()
        Select(self.driver.find_element_by_name("passCount")).select_by_value(passCount)
        Select(self.driver.find_element_by_name("fromPort")).select_by_value(fromPort)
        Select(self.driver.find_element_by_name("fromMonth")).select_by_value(fromMonth)
        Select(self.driver.find_element_by_name("fromDay")).select_by_value(fromDay)
        Select(self.driver.find_element_by_name("toPort")).select_by_value(toPort)
        Select(self.driver.find_element_by_name("toMonth")).select_by_value(toMonth)
        Select(self.driver.find_element_by_name("toDay")).select_by_value(toDay)
        self.driver.find_element_by_xpath("//input[@name='servClass' and @value='" + servClass + "']").click()
        time.sleep(3)
        self.driver.find_element_by_name("findFlights").click()

    def test_select_flight(self, outFlight, inFlight):
        self.driver.find_element_by_xpath("//input[contains(@value,'" + outFlight + "')][@name='outFlight']").click()
        self.driver.find_element_by_xpath("//input[contains(@value,'" + inFlight + "')][@name='inFlight']").click()
        time.sleep(3)
        self.driver.find_element_by_name("reserveFlights").click()
# Este método se ejecuta al final y cierra el navegador
    @ classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("prueba completada con éxito")

if __name__ == '__main__':
    unittest.main()