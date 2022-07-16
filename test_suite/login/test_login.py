import pytest
from time import sleep
from page_object.login_page import LoginPage
from config.loadyaml import loadyaml
from selenium import webdriver


class Test_Login:
	def setup(self) -> None:
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()

	def teardown(self) -> None:
		self.driver.quit()

	@pytest.mark.parametrize('login_data',loadyaml('/Users/Administrator/PycharmProjects/Gaussian_CloudPlatform_UIauto/data/userinfo.yaml'))
	def test_Login(self, login_data):
		a = LoginPage(self.driver).login(login_data['username'], login_data['password'])
		assert login_data['assert'] in a


if __name__ == '__main__':
    pytest.main(['-s','-v'])