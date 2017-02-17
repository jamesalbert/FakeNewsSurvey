from faker import Faker
from random import choice
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

fake = Faker()

answers = [
    'id_question_3382_1',
    'id_question_3383_0',
    'id_question_3384_0',
    'id_question_3385_1',
    ['id_question_3387_1', 'id_question_3387_2', 'id_question_3387_3'],
    {'id_question_3390': ['associated press', 'reuters', 'twitter', 'reddit']},
    'id_question_3392_0_0',
    'id_question_3393_0_1',
    'id_question_3394_0_1',
    {
        'id_question_3395_0_Other': {
            'id_question_3395_1': 'wrong'
        }
    },
    'id_question_3396_0_1',
    'id_question_3397_0_1',
    'id_question_3399_0_1',
    'id_question_3400_0_1',
    'id_question_3402_0_1',
    'id_question_3403_0_1',
    'id_question_3404_0_1',
    'id_question_3406_0_1',
    'id_question_3407_0_1',
    {
        'id_question_3408_0_Other': {
            'id_question_3408_1': 'republicans did obstruct obama and it was reported'
        }
    },
    'id_question_3409_0_1',
    'id_question_3410_0_1',
    'id_question_3411_1',
    {
        'id_full_name': fake.first_name() + " " + fake.last_name()
    },
    {
        'id_email': fake.email()
    },
    {
        'id_postal_code': fake.postcode().split('-')[0]
    }
]


def get(id):
    return driver.find_element_by_id(id)


def take_survey(el):
    if isinstance(el, str) and 'id_' in el:
        get(el).click()
    elif isinstance(el, list):
        get(choice(el)).click()
    elif isinstance(el, dict):
        k = next(iter(el))
        get(k).click()
        if el[k] == 'id_email':
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "id_email"))
        )
        if isinstance(el[k], str):
            get(k).click()
            actions = ActionChains(driver)
            actions.send_keys(el[k])
            actions.perform()
            # get(k).send_keys(el[k])
        elif isinstance(el[k], list):
            get(k).send_keys(choice(el[k]))
        elif isinstance(el[k], dict):
            take_survey(el[k])

for i in range(57000000):
    try:
        driver = webdriver.Chrome('/Users/jbert/Downloads/chromedriver')
        # driver = webdriver.Remote(
        #    command_executor='http://127.0.0.1:4444',
        #    desired_capabilities=DesiredCapabilities.CHROME)
        driver.get("http://action.donaldjtrump.com/mainstream-media-accountability-survey/")
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "id_question_3382_1"))
        )
        for answer in answers:
            take_survey(answer)
        driver.find_element_by_name('respond').click()
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "main"))
        )
        driver.quit()
    finally:
        pass
