from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from datetime import date
from pathlib import Path
class Test_Odev:
    def setup_method(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderpath=str(date.today())
        Path(self.folderpath).mkdir(exist_ok=True)
    #her testen sonra cağırılır
    def teardown_method(self):
        self.driver.quit()
       
    def test_emptyUsernameAndPassword(self):
        self.waitForElementVisible(((By.ID,"user-name")))
        usernameinput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible(((By.ID,"password")))
        passwordinput=self.driver.find_element(By.ID,"password")
        loginButton=self.driver.find_element(By.ID,"login-button")
        # actions=ActionChains(self.driver)
        # actions.send_keys_to_element(usernameinput,"")
        # actions.send_keys_to_element(passwordinput,"")
        # actions.perform()
        loginButton.click()
        self.driver.save_screenshot(f"{self.folderpath}/test-invalid-login-undefinedusername-undefinedpassword.png")
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        self.waitForElementVisible(((By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")))
        assert errorMessage.text=="Epic sadface: Username is required"
    @pytest.mark.parametrize("username",[("1"),("kullaniciadim")]) 
    def test_emptyPassword(self,username):
        self.waitForElementVisible(((By.ID,"user-name")))
        usernameinput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible(((By.ID,"password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameinput,username)
        actions.perform()
        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        self.driver.save_screenshot(f"{self.folderpath}/test-invalid-login-anything-undefinedpassword.png")
        self.waitForElementVisible(((By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")))
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        assert errorMessage.text=="Epic sadface: Password is required"
    def test_userLocked(self):
        self.waitForElementVisible(((By.ID,"user-name")))
        usernameinput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible(((By.ID,"password")))
        passwordinput=self.driver.find_element(By.ID,"password")
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameinput,"locked_out_user")
        actions.send_keys_to_element(passwordinput,"secret_sauce")
        actions.perform()
        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        self.driver.save_screenshot(f"{self.folderpath}/test-userlocked-{usernameinput}-{passwordinput}.png")
        self.waitForElementVisible(((By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")))
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        assert errorMessage.text=="Epic sadface: Sorry, this user has been locked out."    
    def test_userStandart(self):
        self.waitForElementVisible(((By.ID,"user-name")))
        usernameinput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible(((By.ID,"password")))
        passwordinput=self.driver.find_element(By.ID,"password")
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameinput,"standard_user")
        actions.send_keys_to_element(passwordinput,"secret_sauce")
        actions.perform()
        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        normalUrl=self.driver.current_url
        self.driver.save_screenshot(f"{self.folderpath}/test-standart-{usernameinput}-{passwordinput}.png")
        assert normalUrl.endswith("/inventory.html")
    def test_userProblem(self):
        self.waitForElementVisible(((By.ID,"user-name")))
        usernameinput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible(((By.ID,"password")))
        passwordinput=self.driver.find_element(By.ID,"password")
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameinput,"problem_user")
        actions.send_keys_to_element(passwordinput,"secret_sauce")
        actions.perform()
        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        normalUrl=self.driver.current_url
        self.driver.save_screenshot(f"{self.folderpath}/test-problem-{usernameinput}-{passwordinput}.png")
        assert normalUrl.endswith("/inventory.html")
    def test_userCountProducts(self):
        self.waitForElementVisible(((By.ID,"user-name")))
        usernameinput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible(((By.ID,"password")))
        passwordinput=self.driver.find_element(By.ID,"password")
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameinput,"standard_user")
        actions.send_keys_to_element(passwordinput,"secret_sauce")
        actions.perform()
        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        self.waitForElementVisible((By.CLASS_NAME,"inventory_item"))
        testMany=self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        self.driver.save_screenshot(f"{self.folderpath}/test-count-{usernameinput}-{passwordinput}.png")
        assert len(testMany)==6
    
    def test_closeX(self):
        self.waitForElementVisible(((By.ID,"login-button")))
        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        icon_username = self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
        icon_password = self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
        errorMesage=self.driver.find_element(By.CLASS_NAME,"error-button")
        errorMesage.click()
        try:
            icon_username.is_displayed()
            icon_password.is_displayed()
            self.driver.save_screenshot(f"{self.folderpath}/test-closex-false-.png")
            assert False
        except:
            self.driver.save_screenshot(f"{self.folderpath}/test-closex-true-.png")
            assert True
                
    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))    