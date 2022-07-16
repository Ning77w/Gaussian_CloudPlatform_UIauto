import pytest
from page_object.eventcenter.EventDefinition_page import EventDefinition
from config.loadyaml import loadyaml
from page_object.login_page import LoginPage


class Test_EventDefinition():
	# def setup_class(cls) -> None:
	# 	cls.driver = webdriver.Chrome()
	# 	cls.driver.maximize_window()
	#
	# def teardown_class(cls) -> None:
	# 	cls.driver.quit()

	@pytest.fixture(scope='session')
	def Login(self, drivers, username='superadmin', password='123'):
		LoginPage(drivers).login(username, password)

	@pytest.mark.usefixtures('Login')
	@pytest.mark.parametrize('eventsearch_data',loadyaml('/Users/Administrator/PycharmProjects/Gaussian_CloudPlatform_UIauto/data/eventcenter.yaml', 'Searchdata'))
	def test_EventSearch(self, drivers, eventsearch_data):
		EventDefinition(drivers).OpenEventDefinition()
		result = EventDefinition(drivers).SearchEventDefinition(eventsearch_data['eventcode'], eventsearch_data['eventname'])
		assert eventsearch_data['assert'] == result

	def test_ClearSearch(self, drivers):
		result = EventDefinition(drivers).ClearSearchEventDefinition()
		assert True == result

	@pytest.mark.parametrize('status_data', loadyaml('/Users/Administrator/PycharmProjects/Gaussian_CloudPlatform_UIauto/data/eventcenter.yaml', 'Eventstatus'))
	def test_EditEvent(self, drivers, status_data):
		result = EventDefinition(drivers).EditEventStatus()
		assert status_data['status_assert'] in result

	@pytest.mark.parametrize('fre_data', loadyaml('/Users/Administrator/PycharmProjects/Gaussian_CloudPlatform_UIauto/data/eventcenter.yaml', 'Frequency'))
	def test_EditFilterFrequency(self, drivers, fre_data):
		assert True == EventDefinition(drivers).EditEventFilterFrequency(fre_data['fre'])

	@pytest.mark.parametrize('assertdata', loadyaml('/Users/Administrator/PycharmProjects/Gaussian_CloudPlatform_UIauto/data/eventcenter.yaml', 'FieldConfig'))
	def test_FieldConfigPage(self, drivers, assertdata):
		assert True == EventDefinition(drivers).FieldConfigPageView(assertdata['assertdata'])





if __name__ == '__main__':
    pytest.main(['-v'])