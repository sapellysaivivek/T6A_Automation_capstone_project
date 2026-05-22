import json

from selenium.webdriver.common.by import By

from ai.dom_parser import extract_elements
from ai.healing_prompt import build_healing_prompt
from ai.openai_client import ask_openai


BY_MAPPING = {
    "id": By.ID,
    "xpath": By.XPATH,
    "css": By.CSS_SELECTOR,
    "class": By.CLASS_NAME,
    "name": By.NAME
}
def heal_locator(driver, failed_locator):

    available_elements = extract_elements(driver)

    prompt = build_healing_prompt(
        failed_locator,
        available_elements
    )

    response = ask_openai(prompt)

    healed_locator = json.loads(response)

    strategy = healed_locator["strategy"]
    value = healed_locator["value"]

    element = driver.find_element(
        BY_MAPPING[strategy],
        value
    )

    return element