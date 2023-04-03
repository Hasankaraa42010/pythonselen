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
class Test_Demo:
    #her testen once cağırılır
    def setup_method(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderpath=str(date.today())
        Path(self.folderpath).mkdir(exist_ok=True)
    #her testen sonra cağırılır
    def teardown_method(self):
        self.driver.quit()   
    def test_demo(self):
        print("demo test")
    def test_demo_function(self):
        text="Hello"
        assert text=="Hello"
    #testi gecmek için @pytest.mark.skip()     
    @pytest.mark.parametrize("username,password",[("1","1"),("kullaniciadim","sifrem")])   
    def test_invalid_login(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"),10)
        
        usernameinput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        
        passwordinput=self.driver.find_element(By.ID,"password")
        
        usernameinput.send_keys(username)
        passwordinput.send_keys(password)
        
        loginBtn=self.driver.find_element(By.ID,"login-button")
        
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        self.driver.save_screenshot(f"{self.folderpath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text=="Epic sadface: Username and password do not match any user in this service"    
    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))    