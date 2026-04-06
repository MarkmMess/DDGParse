from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

def get_info(driver, url_to_find, position=0) -> tuple[str | None, int]:
    ret = None
    element = driver.find_elements(By.CLASS_NAME, "pAgARfGNTRe_uaK72TAD")

    for el in element[position:]:
        position += 1
        link = el.find_element(By.TAG_NAME, "span")

        if link.text.startswith(f"https://{url_to_find}"):
            found = link.text
            return f"{found} is found at {position} position", position

    return ret, position


def find_site_position(request, url_to_find):
    # You can switch the browser to Chrome, Edge, Firefox, Ie or Safari
    driver = webdriver.Chrome()
    position = 0
    result = None
    url = f"https://duckduckgo.com/?ia=web&origin=funnel_home_google&t=h_&q={request}&chip-select=search"
    driver.get(url)
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CLASS_NAME, "pAgARfGNTRe_uaK72TAD"))
    )
    for number in range(1, 6):

        if number >= 2:
            button = driver.find_element(By.ID, "more-results")
            button.click()
            time.sleep(2)

        result, position = get_info(driver, url_to_find, position)

        if result is not None:
            result = result + f", from page {number}"
            break

    driver.quit()

    return result


req = (input("enter your request: ")).strip()
find_url = (input("""enter url to find it's position: """)).strip()


print(find_site_position(req, find_url))
