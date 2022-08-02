import pytest
from page_object.eventcenter.EventLanguage_page import EventLanguage
from config.loadyaml import loadyaml
from page_object.login_page import LoginPage


class Test_EventLanguage():

    @pytest.fixture(scope='session')
    def Login(self, drivers, username='superadmin', password='123'):
        LoginPage(drivers).login(username, password)

    def test_LanguageTempaltePageview(self, drivers):
        assert True == EventLanguage(drivers).LanguageTempalteOverview()

    @pytest.mark.parametrize('search_data', loadyaml('/Users/Administrator/PycharmProjects/Gaussian_CloudPlatform_UIauto/data/eventcenter.yaml','LauguageSearchdata'))
    def test_SearchLanguageTemplate(self, drivers, search_data):
        assert True == EventLanguage(drivers).SearchLanguageTemplate(search_data['eventcode'],search_data['eventname'],search_data['assert'])




