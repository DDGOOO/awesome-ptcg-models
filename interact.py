from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

# Log in and start(default mode)
def login():
    url = "https://dev.tcgone.net"
    username_or_email = "your_username_or_email"
    password = "your_password"

    driver.maximize_window()
    driver.implicitly_wait(20)

    driver.get(url)
    driver.find_element(By.NAME, "email").send_keys(username_or_email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, '/html/body/div/form/button').click()
    assert "TCG ONE" in driver.title
    driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[3]/div/div/div[5]/div').click()

# Select enabled cards
def select_cards():
    # driver.execute_script("document.body.style.zoom='90%'")

    '''
    TODO: Even when trainer card or energy card has been played,
          they are still recoganized as enabled_cards because in HTML 
          their class_name haven't been changed.
    '''

    # Hand
    while True:
    # for i in range(3):
        try:
            enabled_cards = driver.find_elements(By.CSS_SELECTOR, ".v-image.v-widget.card.v-image-card.card-selectable.v-image-card-selectable.v-has-width")
            selected_card = random.choice(enabled_cards)
            ActionChains(driver).move_to_element(selected_card).perform()
            ActionChains(driver).click().perform()
        except:
            break
    
    # Active pokemon
    while True:
        try:
            active_pokemons = driver.find_elements(By.CSS_SELECTOR, ".v-image v-widget.v-has-width.v-has-height.card.v-image-card.card-selectable.v-image-card-selectable")
            selected_pokemon = random.choice(active_pokemons)
            ActionChains(driver).move_to_element(selected_pokemon).perform()
            ActionChains(driver).click().perform()
        except:
            break

# Take actions
def take_actions():
    # Abilities & Retreat 
    abilities = driver.find_elements(By.CSS_SELECTOR, ".v-button.v-widget.primary.v-button-primary.multiline.v-button-multiline.v-has-width")
    for ability in abilities:
        try:
            desc = ability.find_element(By.XPATH, "./*/*").get_attribute('innerText')
            print(desc)
        except:
            pass

    # End turn
    try:
        driver.find_element(By.CSS_SELECTOR, ".v-button.v-widget.friendly.v-button-friendly.multiline.v-button-multiline.v-has-width").click()
    except:
        pass

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

if __name__ == "__main__":
    login()
    while True:
        select_cards()
        take_actions()
        time.sleep(2)
