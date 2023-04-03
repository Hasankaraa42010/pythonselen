from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



class TestSauceDemo:
    def emptyPassword(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(1)
        username=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        loginButton=driver.find_element(By.ID,"login-button")
        username.send_keys("hasankara")
        sleep(1)
        loginButton.click()
        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        if errorMessage.text=="Epic sadface: Password is required":
            print(f"Test case:{True}")
        else:
            print(f"Test case:{False}")
        while True:
            continue
    def emptyUsernameAndPassword(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(1)
        username=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        if errorMessage.text=="Epic sadface: Username is required":
            print(f"Test case:{True}")
        else:
            print(f"Test case:{False}")
        while True:
            continue
    def userLocked(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(1)
        username=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        loginButton=driver.find_element(By.ID,"login-button")
        username.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginButton.click()
        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        if errorMessage.text=="Epic sadface: Sorry, this user has been locked out.":
            print(f"Test case:{True}")
        else:
            print(f"Test case:{False}")
        while True:
            continue       
    def userStandart(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        
        username=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        loginButton=driver.find_element(By.ID,"login-button")
        username.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButton.click()
        normalUrl=driver.current_url
        if normalUrl.endswith("/inventory.html"):
            testResult=True
            
           
            print(f"Test Sonucu giris:{testResult}")
        else :
            testResult=False
            print(f"Test Sonucu:{testResult}")
        while True:
            continue
    def userCountProducts(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        
        username=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        loginButton=driver.find_element(By.ID,"login-button")
        username.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButton.click()
        
        testMany=driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Ürün sayısı 6 mı:{len(testMany)==6}")
           
           
        while True:
            continue
    def closeX(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        try:
            icon_username = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
            icon_password = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
        except:
            print("İkonlar yok")
        sleep(3)    
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        
        icon_username = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
        icon_password = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
        if icon_username.is_displayed() and icon_password.is_displayed():
            print("ikonlar görünür istendiği gibi")
        else:
            print("Loginde icon gözükmüyor hatalı.")
        sleep(1)
        errorMesage=driver.find_element(By.CLASS_NAME,"error-button")
        sleep(1)
        errorMesage.click()
        try:
            icon_username.is_displayed()
            icon_password.is_displayed()
        except:
            print("ikonlar gitti :True")
        
        while True:
            continue        
        
    


testSauce=TestSauceDemo()
testSauce.closeX()    

    