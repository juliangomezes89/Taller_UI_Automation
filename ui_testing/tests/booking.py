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
        self.driver.find_element_by_link_text("SIGN-OFF").click()
        time.sleep(4)

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

    def test_book_flight_select_2pass(self, passFirst1, passLast1, pass1meal, passFirst2, passLast2, pass2meal):
        self.driver.find_element_by_name("passFirst0").send_keys(passFirst1)
        self.driver.find_element_by_name("passLast0").send_keys(passLast1)
        Select(self.driver.find_element_by_name("pass.0.meal")).select_by_value(pass1meal)
        self.driver.find_element_by_name("passFirst1").send_keys(passFirst2)
        self.driver.find_element_by_name("passLast1").send_keys(passLast2)
        Select(self.driver.find_element_by_name("pass.1.meal")).select_by_value(pass2meal)

    def test_credit_card(self, creditCard, creditnumber, cc_exp_dt_mn, cc_exp_dt_yr, cc_first_name, cc_mid_name, cc_last_name):
        Select(self.driver.find_element_by_name("creditCard")).select_by_value(creditCard)
        self.driver.find_element_by_name("creditnumber").send_keys(creditnumber)
        Select(self.driver.find_element_by_name("cc_exp_dt_mn")).select_by_visible_text(cc_exp_dt_mn)
        Select(self.driver.find_element_by_name("cc_exp_dt_yr")).select_by_value(cc_exp_dt_yr)
        self.driver.find_element_by_name("cc_frst_name").send_keys(cc_first_name)
        self.driver.find_element_by_name("cc_mid_name").send_keys(cc_mid_name)
        self.driver.find_element_by_name("cc_last_name").send_keys(cc_last_name)

    def test_billing_address(self,  billAddress1, billAddress2, billCity, billState, billZip, billCountry):
        self.driver.find_element_by_name("billAddress1").clear()
        self.driver.find_element_by_name("billAddress1").send_keys(billAddress1)
        self.driver.find_element_by_name("billAddress2").send_keys(billAddress2)
        self.driver.find_element_by_name("billCity").clear()
        self.driver.find_element_by_name("billCity").send_keys(billCity)
        self.driver.find_element_by_name("billState").clear()
        self.driver.find_element_by_name("billState").send_keys(billState)
        self.driver.find_element_by_name("billZip").clear()
        self.driver.find_element_by_name("billZip").send_keys(billZip)
        Select(self.driver.find_element_by_name("billCountry")).select_by_value(billCountry)
        self.driver.execute_script("window.alert = function() { return true; }")

    def test_delivery_address(self,  delAddress1, delAddress2, delCity, delState, delZip, delCountry):
        self.driver.find_element_by_name("delAddress1").clear()
        self.driver.find_element_by_name("delAddress1").send_keys(delAddress1)
        self.driver.find_element_by_name("delAddress2").send_keys(delAddress2)
        self.driver.find_element_by_name("delCity").clear()
        self.driver.find_element_by_name("delCity").send_keys(delCity)
        self.driver.find_element_by_name("delState").clear()
        self.driver.find_element_by_name("delState").send_keys(delState)
        self.driver.find_element_by_name("delZip").clear()
        self.driver.find_element_by_name("delZip").send_keys(delZip)
        Select(self.driver.find_element_by_name("delCountry")).select_by_value(delCountry)
        self.driver.execute_script("window.alert = function() { return true; }")
    def test_buyFlights(self):
        self.driver.find_element_by_name("buyFlights").click()
        time.sleep(2)
# Este método se ejecuta al final y cierra el navegador
    @ classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("prueba completada con éxito")

if __name__ == '__main__':
    unittest.main()