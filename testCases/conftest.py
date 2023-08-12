import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://iemodemoindia.meditab.com/#/login?returnUrl=%2Fapp%2Fdashboard")
    yield driver
    driver.quit()


def pytest_metadata(metadata):
    # To Add
    metadata["Tester Name"] = "Sudhir Thool"
    metadata["Batch"] = "CT#15"
    metadata["URL"] = "https://iemodemoindia.meditab.com/#/login?returnUrl=%2Fapp%2Fdashboard"
    # To Remove
    metadata.pop("Platform", None)