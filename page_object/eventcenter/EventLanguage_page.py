from time import sleep
from common_base.selenium_base import selenium_base
from selenium import webdriver
from locator.loc_eventcenter import event_locater, event_language

class EventLanguage(selenium_base):

    #打开并校验语言管理页
    def LanguageTempalteOverview(self):
        self.elements_click(event_language.languageAdministration, '进入语言管理页')
        self.isElementExist(event_language.eventLanguageList)


    def SearchLanguageTemplate(self, eventcode, eventname, Listdata):
        self.elements_click(event_language.languageAdministration, '进入语言管理页')
        self.elements_input(event_locater.eventedit_search, eventcode, '输入事件编码')
        self.elements_input(event_locater.evevtname_search, eventname,'输入事件名称')
        self.elements_click(event_locater.eventsearch, '点击搜索')
        self.in_element(event_language.eventLanguageList, Listdata, Type='text')
