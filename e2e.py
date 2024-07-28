from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys

# Configuration for WebDriver
CHROME_DRIVER_PATH = 'C:/Users/PC/PycharmProjects/wog/ChromeDrive/chromedriver-win64/chromedriver.exe'
URL = 'http://127.0.0.1:8777/'


def test_scores_service(application_url):
    """Test the scores web service to ensure the score is a valid number."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    chrome_service = ChromeService(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    try:
        driver.get(application_url)
        score_element = driver.find_element(By.ID, "score")
        score_text = score_element.text

        # Check if the score is a number between 1 and 1000
        if score_text.isdigit():
            score = int(score_text)
            return 1 <= score <= 1000
        else:
            print("Score is not a valid number.")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        driver.quit()


def main_function():
    """Main function to call test_scores_service and handle exit codes."""
    if test_scores_service(URL):
        print("Tests passed.")
        return 0
    else:
        print("Tests failed.")
        return -1


main_function()
