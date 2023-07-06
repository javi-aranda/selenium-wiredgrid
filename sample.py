import logging

from selenium.webdriver.chrome.options import Options as ChromeOptions
from seleniumwire import webdriver

logger = logging.getLogger(__name__)

def get_chrome_capabilities():
    chrome = ChromeOptions()
    chrome.add_argument("--headless")
    chrome.add_argument("--window-size=1920,1080")
    return chrome.to_capabilities()


def get_seleniumwire_options(proxy):
    return {
        'addr': 'selenium-proxy', # Hostname of container running seleniumwire MITM proxy
        'verify_ssl': False,
        'proxy': {
            'http': proxy,
            'https': proxy
        }
    }


def get_remote_driver(proxy):
    return webdriver.Remote(
        command_executor='http://selenium-hub:4444/wd/hub', # Hostname of Selenium-Grid
        desired_capabilities=get_chrome_capabilities(),
        seleniumwire_options=get_seleniumwire_options(proxy=proxy)
    )


def main():
    proxy = None  # <protocol>://<username>:<password>@<host>:<port>
    logger.info(f"Using proxy: {proxy}")

    logger.info("Starting Selenium WebDriver")
    driver = get_remote_driver(proxy)

    logger.info("Getting IP")
    driver.get('https://ip.me/')

    logger.info("Saving screenshot")
    driver.save_screenshot("my-ip.png")


if __name__ == '__main__':
    main()
