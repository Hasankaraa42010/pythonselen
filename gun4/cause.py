from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
class Test_Sauce:
    def __init__(self):
        
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    def test_invalid_login(self):
        
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameinput=self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordinput=self.driver.find_element(By.ID,"password")
        
        usernameinput.send_keys(1)
        passwordinput.send_keys(1)
        
        loginBtn=self.driver.find_element(By.ID,"login-button")
        
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        testResult=errorMessage.text=="Epic sadface: Username and password do not match any user in this service"
        print(f"Test sonucu:{testResult}")

    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameinput=self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordinput=self.driver.find_element(By.ID,"password")
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameinput,"standard_user")
        actions.send_keys_to_element(passwordinput,"secret_sauce")
        actions.perform()

        # self.driver.execute_script("console.log("mERHABA)") JAVASCRPİT LAZIM OLURSA 

        # usernameinput.send_keys("standard_user")
        # passwordinput.send_keys("secret_sauce")
        
        loginBtn=self.driver.find_element(By.ID,"login-button")
        
        loginBtn.click()

testClass=Test_Sauce()
testClass.test_invalid_login() 
testClass.test_valid_login()