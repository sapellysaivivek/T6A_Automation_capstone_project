from bs4 import BeautifulSoup


def extract_elements(driver):

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")

    elements = []

    buttons = soup.find_all(["button", "input", "a"])

    for element in buttons:

        elements.append({
            "id": element.get("id"),
            "class": element.get("class"),
            "text": element.text.strip(),
            "type": element.name
        })

    return elements