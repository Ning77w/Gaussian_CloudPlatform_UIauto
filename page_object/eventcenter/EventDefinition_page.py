from time import sleep
from common_base.selenium_base import selenium_base
from selenium import webdriver
from locator.loc_eventcenter import event_locater



class EventDefinition(selenium_base):

    #打开事件定义
    def OpenEventDefinition(self):
        self.elements_click(event_locater.sidebar_botton, '展开侧边栏')
        self.elements_click(event_locater.eventcenter, '点击事件中心tab')
        sleep(2)
        self.elements_click(event_locater.eventdefinition, '点击事件定义')

    #搜索事件code
    def SearchEventDefinition(self, eventcode, eventname):
        self.elements_input(event_locater.eventedit_search, eventcode, '输入事件编码')
        self.elements_input(event_locater.evevtname_search, eventname, '输入事件名称')
        # self.select(event_locater.isBlockTask_search, '1', Type='index')
        # self.select(event_locater.incidentLevel_search, '2', Type='index')
        result = self.in_element(event_locater.eventdefinitionpage,'22005', Type='text')
        if result == True:
            self.elements_click(event_locater.eventsearch, '点击搜索')
            result = self.in_element(event_locater.eventdefinitionpage, '22004', Type='text')
        return result

    #清除搜索条件
    def ClearSearchEventDefinition(self):
        self.wait_ele_visible(event_locater.eventlist)
        self.elements_click(event_locater.ClearBotton, '清除搜索条件')
        return self.in_element(event_locater.eventdefinitionpage, '22005', Type='text')


    #新增事件定义
    def AddEventDefinition(self, NewEventcode, NewEventname):
        self.elements_click(event_locater.evevtadd, '点击新增')
        self.elements_input(event_locater.eventedit_search, NewEventcode, '输入事件编号')
        self.elements_input(event_locater.evevtname_search, NewEventname, '输入事件名')
        self.select(event_locater.incidentPartition_search, '2', Type='index')
        self.select(event_locater.incidentLevel_search, '2', Type='index')
        self.select(event_locater.isBlockTask_search, '2', Type='index')
        self.elements_click(event_locater.eventadd_botton, '点击完成')


    #编辑事件开关状态
    def EditEventStatus(self):
        self.elements_click(event_locater.eventstatusBotton, '事件状态编辑')
        sleep(5)
        statusNow = self.get(event_locater.eventstatus, Type='text', name='', page_name='事件列表')
        return statusNow

    #编辑事件过滤频率
    def EditEventFilterFrequency(self, fre):
        sleep(5)
        self.clear_input(event_locater.filterfrequency, '过滤频率')
        self.elements_input(event_locater.filterfrequency, fre, '输入频率')
        self.move_to_coordinate('0', '0')
        return self.in_element(event_locater.filterfrequency, fre, Type='text')

    #校验字段配置页
    def FieldConfigPageView(self, confdata):
        self.elements_click(event_locater.FieldConfig, '字段配置')
        if self.isElementExist(event_locater.fieldConfiglist) == True:
            result = self.in_element(event_locater.fieldConfiglist, confdata, Type='text')
            return result
        else:
            return False












if __name__ == '__main__':
    driver = webdriver.Chrome()
