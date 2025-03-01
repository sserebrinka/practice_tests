from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from list_languages import languages

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_language_verification(browser, request):
    user_language = request.config.getoption("language")

    expected_button_text = None
    for lang in languages:
        if lang[0] == user_language:
            expected_button_text = lang[2]
            break

    assert expected_button_text is not None, f"Language '{user_language}' not found in the list of supported languages."

    browser.get(link)

    # время для проверки текста на кнопке
    time.sleep(5)

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
    )
    button_text = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").text

    assert button_text == expected_button_text, f"Expected button text '{expected_button_text}', but got '{button_text}'"