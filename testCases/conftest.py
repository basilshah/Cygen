from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver


#####HTML Report

def pytest_configure(config):
    config._metadata['Project Name'] = 'Hospital'
    config._metadata['Module Name'] = 'Reception'
    config._metadata['Tester'] = 'Admin'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)