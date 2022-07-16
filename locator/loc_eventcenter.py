from selenium.webdriver.common.by import By


class event_locater:

    #事件中心tab
    eventcenter = (By.XPATH, '//*[@id="root"]/div/section/section/div/aside/div/ul/li[7]/div/span/span')
    #事件定义tab
    eventdefinition = (By.XPATH, '//*[@id="/event$Menu"]/li[1]')
    #事件定义页面
    eventdefinitionpage = (By.CSS_SELECTOR, '#root > div > section > section > main > main > div > div.PageHeaderLayout__content___ZZk9k > div > div')
    #事件定义-添加事件
    evevtadd = (By.XPATH,'//*[@id="root"]/div/section/section/main/main/div/div[3]/div/div/div[1]/form/div[3]/div[3]/span/button[2]')
    #事件定义-搜索
    eventsearch = (By.XPATH,'//*[@id="root"]/div/section/section/main/main/div/div[3]/div/div/div[1]/form/div[2]/div[3]/span/button[2]')
    #事件定义-事件编码
    eventedit_search = (By.CSS_SELECTOR,'#incidentCode')
    #事件定义-事件名称
    evevtname_search = (By.CSS_SELECTOR,'#incidentTitle')
    #事件定义-是否影响任务下拉框
    isBlockTask_search = (By.CSS_SELECTOR,'#isBlockingTask')
    #影响下拉框否元素
    BlockTaskNo = (By.XPATH, '//*[@id="5442c0a3-68e2-4661-952e-62ecde202479"]/ul/li[3]')
    #事件定义-事件等级
    incidentLevel_search = (By.CSS_SELECTOR,'#incidentLevel')
    #事件定义-运维类型
    incidentPartition_search = (By.XPATH,'//*[@id="incidentPartition"]')
    #事件新增完成
    eventadd_botton = (By.CSS_SELECTOR,'body > div:nth-child(3) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button.ant-btn.ant-btn-primary')
    #事件定义-清空搜索条件
    ClearBotton = (By.CSS_SELECTOR,'#root > div > section > section > main > main > div > div.PageHeaderLayout__content___ZZk9k > div > div > div.EventCenter__formContainer___lSEwB > form > div:nth-child(2) > div:nth-child(3) > span > button:nth-child(1)')
    #事件定义-导入事件
    importBotton = (By.XPATH,'//*[@id="root"]/div/section/section/main/main/div/div[3]/div/div/div[1]/form/div[3]/div[3]/span/div/span/div[1]/span/button')
    #事件定义-导出事件
    exportBotton = (By.XPATH,'//*[@id="root"]/div/section/section/main/main/div/div[3]/div/div/div[1]/form/div[3]/div[3]/span/button[1]/span')
    #事件定义-事件状态按钮
    eventstatusBotton = (By.CSS_SELECTOR, '#root > div > section > section > main > main > div > div.PageHeaderLayout__content___ZZk9k > div > div > div.ant-table-wrapper.EventCenter__eventTable___zIkL6 > div > div > div > div > div.ant-table-fixed-left > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > button')
    #事件定义-事件状态
    eventstatus = (By.XPATH,'//*[@id="root"]/div/section/section/main/main/div/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[3]/div/span')
    #事件列表
    eventlist = (By.XPATH,'//*[@id="root"]/div/section/section/main/main/div/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div/table/tbody')
    #事件定义-发送频率
    filterfrequency = (By.CSS_SELECTOR, '#alertFrequency_1')
    #事件定义-字段配置按钮
    FieldConfig = (By.XPATH, '//*[@id="root"]/div/section/section/main/main/div/div[3]/div/div/div[1]/form/div[3]/div[3]/span/a/button')
    #字段配置-列表
    fieldConfiglist = (By.XPATH, '//*[@id="root"]/div/section/section/main/main/div/div[3]/div/div/div[2]')


class event_language:
    #多语言管理tab
    languageAdministration = (By.CSS_SELECTOR, '# \/event\$Menu > li:nth-child(2) > a > span')
    # \/event\$Menu > li:nth-child(2) > a > span
    eventLanguageList = (By.XPATH, '//*[@id="root"]/div/section/section/main/main/div/div[3]/div/div/div[2]/div/div/div/div/div[1]/div')