from selenium.webdriver.common.by import By


class login_locater:

    url = "https://home.release.gs-robot.com/apps?redirect=https%3A%2F%2Fcloud.release.gs-robot.com%23%2F#/"
    username = (By.ID, "basic_username")
    password = (By.ID, "basic_password")
    login_botton = (By.XPATH, '//*[@id="basic"]/div[3]/div/div/div/button')
    title = (By.CSS_SELECTOR, 'head > title')
    # Verification = (By.CSS_SELECTOR, '#basic > div:nth-child(3) > div > div > div > div > div.img > div > img')
    # VerificationInput = (By.CSS_SELECTOR, '')
    banner = (By.CSS_SELECTOR, '#root > div > section > header > div > div.index__right___smJRL > span:nth-child(4)')