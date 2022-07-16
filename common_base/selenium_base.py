#coding:utf-8
#file: seleniu_base.py
#@author: zhidongmei
#@time: 2019/10/11 10:56
#@desc: 基于原生的selenium做二次封装,作为基类为页面模型服务
import os,sys,unittest,time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from config import RunConfig
from config.logger import logger



class selenium_base():


    def __init__(self, driver):  # driver:webdriver.Chrome：映射driver 为webdriver.Chrome
        self.driver = driver
        self.timeout = 50
        self.t = 2

    def save_page_shot(self, page_name):
        screenshotname = f"{page_name}__{time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())}.png"
        filename = os.path.join(RunConfig.screenshot_dir, screenshotname)
        self.driver.save_screenshot(filename)
        logger().info(f"当前界面截图成功并保存在：{filename}")
        try:
            self.driver.save_screenshot(screenshotname)
            logger().info("屏幕截图成功，截图存放路径：%s" % screenshotname)
        except NameError as e:
            logger().error("屏幕截图失败：%s" % e)

    def load_page(self, env_url):
        logger().info(f"在访问{env_url}")
        try:
            self.driver.get(env_url)
        except:
            logger().exception(f"driver加载失败")
            self.save_page_shot(env_url)

    def locator(self, loc, page_name):
        logger().info(f"在{page_name}定位元素{loc}")
        try:
            ele = self.driver.find_element(*loc)
        except:
            logger().exception("元素定位失败")
            self.save_page_shot(page_name)
            raise
        return ele


    def find_elements(self, loc, value=''):
        '''查找页面元素信息，入参为元组形式，key：定位方式，value：元素值'''
        logger().info(f"正在定位元素信息：定位方式->{loc[0]}, 元素值->{loc[1]}，value值->{value}")
        try:
            if isinstance(loc, tuple):
                if value != '':  # value值定位
                    ele = WebDriverWait(self.driver, self.timeout, self.t).until(
                        EC.text_to_be_present_in_element_value(loc, value))
                    return ele
                else:  # 默认为此常规定位方法
                    ele = WebDriverWait(self.driver, self.timeout, self.t).until(
                        EC.presence_of_element_located(loc))
                    if ele:
                        return ele
        except:
            logger().exception('locator参数类型错误，必须传元组类型：loc = ("id", "value1")')
            return False

    def elements_input(self, loc, input_info, page_name):
        '''输入框输入，二次封装send_keys能力'''
        logger().info(f"在{page_name}当前位置{loc}输入{input_info}")
        try:
            self.find_elements(loc).send_keys(input_info)
        except:
            logger().exception("输入失败！")
            self.save_page_shot(page_name)

    def elements_click(self, loc, page_name):
        '''点击操作，入参为tuple'''
        logger().info(f"在{page_name}{loc}点击操作")
        try:
            self.find_elements(loc).click()
        except:
            logger().info("点击失败！")
            self.save_page_shot(page_name)


    def clear_input(self, loc, page_name):
        logger().info(f"在{page_name}{loc}点击操作")
        '''清空输入框输入'''
        try:
            self.find_elements(loc).clear()
        except:
            logger().error("目标元素清除失败")
            self.save_page_shot(page_name)


    def isSelected(self, locator, Type=''):
        ''' 判断元素是否被选中，返回bool值 及点（选中/取消选中）'''
        ele = self.find_elements(locator)
        try:
            if Type == '':  # 如果type参数为空，返回元素是否为选中状态，True/False (默认)
                r = ele.is_selected()
                return r
            elif Type == 'click':  # 如果type参数为click，执行元素的点击操作
                ele.click()
            else:
                print(f"type参数 {Type} 错误，仅可为click或''")
        except:
            return False

    def isElementExist(self, locator):
        ''' 判断单个元素是否在DOM里面 （是否存在）'''
        try:
            self.find_elements(locator)
            return True
        except:
            return False

    def isElementExists(self, locator):
        ''' 判断一组元素是否在DOM里面 （是否存在），若不存在，返回一个空的list'''
        eles = self.find_elements(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print(f"定位到元素的个数：{n}")
            return True

    def title(self, title, Type='contains'):
        '''  根据传入的type类型判断title  '''
        try:
            if Type == 'is':  # 判断当前网页title名为title   返回bool值
                result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
                return result
            elif Type == 'contains':  # 判断当前网页title名含title   返回bool值 (默认)
                result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
                return result
            else:
                print(f"type参数 {Type} 错误，仅可为is、contains")
        except:
            return False

    def in_element(self, locator, value, Type='text'):
        '''  根据传入的type判断内容是否在指定元素里面  '''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc = ("id", "value1")')
        try:
            if Type == 'text':  # 判断当前获取到的text含value   返回bool值 （默认）
                result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, value))
                return result
            elif Type == 'value':  # 判断当前获取到的value含value 返回bool值, value为空字符串，返回False
                result = self.find_elements(locator, value)
                return result
            else:
                print(f"type参数 {Type} 错误，仅可使用text或value属性定位")
                return False
        except:
            return False

    def alert(self, timeout=3, Type=''):
        ''' 根据传入的type判断alert弹窗及操作 '''
        result = WebDriverWait(self.driver, timeout, self.t).until(EC.alert_is_present())
        try:
            if Type == '':  # 判断alert是否存在，如果有，就返回alert对象 （默认）
                if result:
                    return result
                else:
                    print("alert不存在")
                return False
            elif Type == 'yes':  # 执行alert的确定按钮
                result.accept()
            elif Type == 'no':  # 执行alert的取消按钮
                result.dismiss()
            else:
                print(f"type参数 {Type} 错误，仅可为yes、no、或''")
        except:
            return False

    def get(self, locator, Type='text', name='',page_name=''):
        ''' 根据传入的type判断获取指定的内容 （title、text、attribute）
        type==attribute:  获取元素属性  name:属性  className、name、text、value···  '''
        logger().info(f"在{locator}获取内容{Type}")
        try:
            if Type == 'title':  # 获取当前网页 title
                return self.driver.title
            elif Type == 'text':  # 获取元素文本值（默认）
                return self.find_elements(locator).text
            elif Type == 'attribute':  # 获取当前元素属性
                return self.find_elements(locator).get_attribute(name)
            else:
                print(f"给的type参数 {Type} 错误，仅可用title、text、attribute")
        except:
            logger().error(f"获取指定内容{Type}失败")
            self.save_page_shot(page_name)
            return ''

    def select(self, locator, value, Type='index'):
        '''  下拉选项框 根据传入的type值判断（index、value、text）  '''
        element = self.find_elements(locator)  # 定位select这一栏
        try:
            if Type == 'index':  # 用下标选择 （默认）
                Select(element).select_by_index(value)
            elif Type == 'value':  # 根据value值选择
                Select(element).select_by_value(value)
            elif Type == 'text':  # 根据选项的文本内容选择
                Select(element).select_by_visible_text(value)
            else:
                print(f"给的type参数 {Type} 错误，仅可为：int、text、value")
        except:
            print(f"根据 {value} 操作下拉框失败")

    def iframe(self, id_index_locator):
        ''' 常规切换 iframe'''
        try:
            if isinstance(id_index_locator, int):  # 如果传入的是数字，则以该数字为下标取值
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, str):  # 如果传入的是字符串，则用iframe名字取值
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, tuple):  # 如果是元组，则根据传入的locator取值
                ele = self.find(id_index_locator)
                self.driver.switch_to.frame(ele)
        except:
             print("iframe切换异常")

    def handle(self, value):
        ''' 句柄切换，index、句柄名 '''
        try:
            if isinstance(value, int):  # 切换到该下标对应的窗口
                handles = driver.window_handles
                self.driver.switch_to.window(handles[value])
            elif isinstance(value, str):  # 切换到该句柄名称对应的窗口
                self.driver.switch_to.window(value)
            else:
                print(f"传入的type参数 {value} 错误，仅可传int、str")
        except:
            print(f"根据 {value} 获取句柄失败")

    def move_to_element(self, locator):
        ''' 鼠标悬停操作 '''
        try:
            ele = self.find(locator)
            ActionChains(self.driver).move_to_element(ele).perform()
        except:
            print("鼠标悬停操作失败")
            return False


    def move_to_coordinate(self, horizontal, longitudinal):
        '''鼠标移动到特定坐标，点击'''
        try:
            ActionChains(self.driver).move_by_offset(horizontal, longitudinal).click().perform()
        except:
            logger().error("点击特定坐标失败")
            return False



    def wait_ele_visible(self, loc, timeout=60, poll_frequency=0.5):
        ''' 等待页面元素可见 '''
        WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)


    def page_refresh(self):
        try:
            self.driver.refresh()
        except:
            logger().exception("刷新当前页失败")


    '''==============================js与jQuery相关====================================='''

    def js_focus_element(self, locator):
        ''' 聚焦元素 '''
        target = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        ''' 滚动到顶部 '''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self, x=0):
        ''' 滚动到底部 '''
        js = f"window.scrollTo({x},document.body.scrollHeight)"
        self.driver.execute_script(js)

    def js_find(self, action):
        '''  js查找元素，并做相应操作（默认id属性） 输入值：value='XXX'  点击：click() '''
        js = f"document.getElementById(“id”).{action}"
        self.driver.execute_script(js)

    def js_finds(self, Type, element, index, action):
        '''   js查找元素，并做相应操作   输入值：value='XXX'     点击：click()
        js定位仅可为：id、Name、TagName、ClassName、Selector（CSS） '''
        list = ['Name', 'TagName', 'ClassName', 'Selector']
        if type in list:
            print(f"正在执行js操作：定位方式->{Type}, 元素值->{element}， 下标值->{index}， 执行操作->{action}")
            if type == 'Selector':
                js = f'document.query{Type}All("{element}"){index}.{action}'
            else:
                js = f'document.getElementsBy{Type}({element})[{index}].{action};'
            self.driver.execute_script(js)
        else:
            print(f"type参数 {Type} 错误，js定位仅可为：'Name'、'TagName'、'ClassName'、'Selector'（CSS）")

    def js_readonly(self, idElement, value):
        ''' 去掉只读属性，并输入内容 一般为id '''
        js = f'document.getElementById({idElement}).removeAttribute("readonly");document.getElementById({idElement}).value="{value}"'
        driver.execute_script(js)

    def js_iframe(self, Type, element, action, index=''):
        '''  Js处理iframe   无需先切换到iframe上，再切回来操作
        输入值：value=''         点击：click()           type=id时，index=''  '''
        js = f'document.getElementBy{Type}({element}){index}.contentWindow.document.body.{action}'
        driver.execute_script(js)

        jquery = '$(CSS).val("XXX");'   # 根据css语法定位到元素，输入内容
        jquery = '$(CSS).val('');'      # 清空
        jquery = '$(CSS).click();'      # 点击
        driver.execute_script(jquery)


    def switch_alert(self):
         ''' 获取alert弹窗 '''
         r = self.is_alert()
         if not r:
             print("alert不存在")
         else:
             return r

    def is_title(self, title):
         '''判断当前title名为title   返回bool值'''
         try:
             result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
             return result
         except:
             return False
    def is_title_contains(self, title):
         '''判断当前title名含title   返回bool值'''
         try:
             result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
             return result
         except:
             return False

    def is_text_in_element(self, locator, _text=''):
         '''判断当前获取到的text含_text=''   返回bool值'''
         if not isinstance(locator, tuple):
             print('locator参数类型错误，必须传元组类型：loc = ("id", "value1")')
         try:
             result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, _text))
             return result
         except:
             return False



    def is_value_in_element(self, locator, _value=''):
         '''返回bool值, value为空字符串，返回False'''
         if not isinstance(locator, tuple):
             print('locator参数类型错误，必须传元组类型：loc = ("id", "value1")')
         try:
             result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator, _value))
             return result
         except:
             return False

    def get_title(self):
         '''获取title'''
         return self.driver.title

    def get_text(self, locator):
         '''获取文本'''
         try:
             t = self.find(locator).text
             return t
         except:
             print("获取text失败，返回'' ")
             return ""


    def get_attribute(self, locator, name):
         '''获取属性'''
         try:
             element = self.find(locator)
             return element.get_attribute(name)
         except:
             print("获取%s属性失败，返回'' "%name)
             return ""

    def select_by_index(self, locator, index=0):
          '''通过索引,index是索引第几个，从0开始，默认选第一个'''
          element = self.find(locator)  # 定位select这一栏
          Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
         '''通过value属性'''
         element = self.find(locator)
         Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
         '''通过文本值定位'''
         element = self.find(locator)
         Select(element).select_by_visible_text(text)

    def switch_handle_window_name(self, window_name):
         ''' 根据句柄名字切换句柄 '''
         self.driver.switch_to.window(window_name)

    def switch_handle_index(self, index):
         '''  根据句柄下标切换句柄  '''
         handles = driver.window_handles
         self.driver.switch_to.window(handles[index])

    def js_findelement(self, action):
         '''
         输入值：value='XXX'     点击：click()
         '''
         print("正在执行js操作，操作行为：%s"%action)
         js = "document.getElementById(“id”).%s"%action
         self.driver.execute_script(js)

if __name__ == "__main__":
    driver = webdriver.Chrome()