import time
from selenium.webdriver.common.by import By

def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    time.sleep(30)
    
    buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    
    assert len(buttons) > 0, "Button 'Add to basket' was not found on the product page!"
