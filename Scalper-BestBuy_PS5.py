import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

bought=0
while (bought<1):

    #Block images from options to load faster
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    
    driver = webdriver.Chrome(executable_path="C:\\Users\\rguadamuz\\Documents\\Python\\Selenium\\chromedriver.exe", options=chrome_options)
    
    driver.set_page_load_timeout(30)
    driver.maximize_window()
    
    driver.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149") #BestBuy PS5 Console Standard (Sold Out)
    
    buyButton = False
    
    while not buyButton:
        try:
            #Buy button is not yet available
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"btn-disabled")))
            driver.find_element_by_class_name("btn-disabled")
            t=time.strftime("%H:%M:%S", time.localtime())
            print(t + " Add-to-cart button is not ready yet.")
    
            time.sleep(15) #Wait some time and refresh page
            driver.refresh()
            
        except:
            print("Add-to-cart button available.")
            driver.find_element_by_class_name("fulfillment-add-to-cart-button").click()
            print("Add-to-cart button was clicked.")
            
            buyButton = True #exit while loop and continue shopping
            
            
    #Go to cart
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"go-to-cart-button")))
    driver.find_element_by_class_name("go-to-cart-button").click()
    print("Go-to-cart button was clicked.")
    
    #Continue to checkout
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"checkout-buttons__checkout")))
    driver.find_element_by_class_name("checkout-buttons__checkout").click()
    print("Checkout button was clicked.")
    
    #Continue as guest
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"button-wrap")))
    driver.find_element_by_class_name("button-wrap").click()
    print("Continue-as-guest button was clicked.")
    
    #Fill email and phone number
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"user.emailAddress")))
    driver.find_element_by_id("user.emailAddress").send_keys("your_email@gmail.com")
    print("Email input in the form.")
    
    driver.find_element_by_id("user.phone").send_keys("123456789")
    print("Phone input in the form.")
    
    #Continue to payment
    driver.find_element_by_class_name("button--continue").click()
    print("Continue-to-payment-information button was clicked.")
    
    #Credit card information
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"optimized-cc-card-number")))
    driver.find_element_by_id("optimized-cc-card-number").send_keys("1234567890123456")
    driver.find_element_by_name("expiration-month").send_keys("01")
    driver.find_element_by_name("expiration-month").send_keys("21")
    driver.find_element_by_id("credit-card-cvv").send_keys("999")
    print("Credit card information input in the form.")
    
    #Billing address
    driver.find_element_by_id("payment.billingAddress.firstName").send_keys("Name")
    driver.find_element_by_id("payment.billingAddress.lastName").send_keys("Last name")
    driver.find_element_by_id("payment.billingAddress.street").send_keys("Address")
    driver.find_element_by_id("payment.billingAddress.street").send_keys(Keys.DOWN, Keys.ENTER)
    driver.find_element_by_id("payment.billingAddress.city").send_keys("City")
    driver.find_element_by_id("payment.billingAddress.state").send_keys("State")
    driver.find_element_by_id("payment.billingAddress.zipcode").send_keys("Zip code")
    print("Billing Address input in the form.")
    
    #Place order
    driver.find_element_by_class_name("button--place-order").click()
    print("Order submitted.")
    
    bought=bought+1
    time.sleep(3)
    driver.get_screenshot_as_file("BestBuy_PS5-Standard_Receipt_"+str(bought)+".png")
#driver.quit()

