import os
import yaml
from selenium import webdriver


PRO_PATH = os.path.dirname(os.path.abspath(__file__))
class RunConfig:
    '''
    运行配置
    '''
    #测试用例目录
    cases_path = os.path.join(PRO_PATH, "test_suite")

    #浏览器驱动类型
    driver_type = "chrome"

    #失败重跑次数
    rerun = '3'

    #最大失败数
    max_fail = '5'

    #报告生成路径
    Report = None

    #运行线程数
    Thread = '4'

    #MySql配置
    mysql_ip = 'localhost'
    mysql_port = '3306'
    db_name = ''
    db_username = ''
    db_password = ''
    mysql_charset = 'utf - 8'



# 获取根目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
# 用例目录
case_dir = os.path.join(base_dir, "test_case")
print(case_dir)
# 日志路径
logs_dir = os.path.join(base_dir, "output/log")
print(logs_dir)
# 截图路径
screenshot_dir = os.path.join(base_dir, "output/Screenshots")
print(screenshot_dir)
# 测试报告
report_dir = os.path.join(base_dir, "output/Report")
# 数据路径
casedatas_dir = os.path.join(base_dir, "data")
print("----------------------------------------------------------")

# 全局
def get_project_path():
    '''全局：获得项目路径'''
    realpath = os.path.dirname(__file__).split('common')[0]
    return realpath

# 读取yaml配置文件
def get_yaml_config(one_name, two_name):
    '''全局：读取全局配置yaml文件'''
    with open(str(get_project_path()) + 'config.yaml', 'r', encoding='utf-8') as f:
        cfg = yaml.load(f.read(), Loader=yaml.FullLoader)
        return cfg[one_name][two_name]

if __name__ == '__main__':
    print(get_project_path())