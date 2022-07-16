import pytest
from time import sleep
from page_object.login_page import LoginPage
from config.loadyaml import loadyaml
from selenium import webdriver



driver = None

@pytest.fixture(scope= 'session')
def drivers(request):
	global driver
	if driver is None:
		driver = webdriver.Chrome()
		driver.maximize_window()
	def fn():
		driver.quit()
	request.addfinalizer(fn)
	return driver

