[toc]

python + selenium + pytest + PageObject + Allure + 元素抽象 + mysql + 多线程 + img 截图 + log 日志 + 多浏览器支持 + 全参数化构建  

# 1.框架注意点-使用前必看
- 项目完全依靠参数化构建，见文件`Gaussian_CloudPlatform_UIauto\config\RunConfig.py`
- `test_suite` 中存放测试用例，测试用例需要以 test_ 打头，测试类以Test_或GusssianTest_打头，
- `page_object`中存放 PO 对象，抽象页面中的功能领域模型
- 此项目在我电脑中采用本地环境，所以git拉取后自行下载所需依赖，下方已给出
- `data`存放数据，采用pytest.mark数据驱动，所有测试数据和断言数据均在此目录中
- 测试报告和allure结果存放在根目录文件夹下，可根据需要修改配置路径
- 建议用谷歌和火狐驱动，ie 似乎元素定位不一样

# 2.所需依赖
本人使用的是 python 3.9
```
pytest          7.1.2
selenium        4.3.0
PyMySQL         0.9.3
Allure-pytest   2.9.45
Allure package  2.18.1     git:https://github.com/allure-framework/allure2/releases
pip             20.2.3	
redis           3.3.11
Pyyaml          6.0	
tomorrow        0.2.4	
urllib3         1.25.7	
tesserate       0.1.3
```

# 3.项目结构
```
Gaussian_CloudPlatform_UIauto
    - allure-results（allure的json报告）
    - common_base（封装selenium、webdriver、tesserate（验证码识别）等基类）
        - selenium_base（封装selenium和webdriver，源文件copy自大姐，有新需求可在其中自行封装）
        - tesserate（验证码识别，待实现）
    - config（项目配置）
        - loadyaml（实现yaml格式的读写）
        - logger（定义日志）
        - logger_util (log工具类)
        - RunConfig (启动配置，包括各种路径、重跑次数、线程数、驱动类型等)
    - data（存放测试数据和断言数据，根据业务类别写入对应的yaml文件）
    - locator（所有元素的集合）
    - output (log和截图存放路径)
    - page_object (业务功能领域模型)
        - evevtcenter (事件中心功能封装)
        - login （登录页功能封装）
        - .../根据业务模型自行创建
    - report （存放allure的html报告）
        - index.html (测试报告)
    - test_suite (测试用例集合)
    - venv（虚拟环境的文件夹，github 拉下来后需要自己创虚拟环境）
    - .gitignore（git 忽略文件）
```

# 4.可以拓展补充的地方
1. 运行多线程 虽然基于pytest原生实现了多线程，但是遇到耦合程度较高的场景并不适用，后续考虑优化
2. 可添加读取 csv，txt 等多种文件的工具类方便读取数据，yaml适合少量测试数据的管理，后期用例量多起来管理并不方便
3. 连接数据库读写和验证码识别的底层虽然已经搭建，但并没有实际应用，为了减少前置造数步骤，需要使用数据库直接创建测试数据
4. 邮件和钉钉发送目前没有做，考虑到后续部署可能采用jenkins方式，可以在jenkins中直接配置  #后续
5. 目前driver是自己配置的，后续可考虑把不同浏览器的driver放在脚本中，执行测试前读取浏览器版本自动更新driver，避免后续的环境配置问题
6. 多浏览器执行需要做自己修改配置文件中的driver，之后可以考虑实现多浏览器的自动执行（chrome、火狐）

# 5.目前痛点
1. 用例执行不稳定，换一套环境或者换一台机器，可能之前执行成功的用例就会失败；解决方案：降低用例间的耦合，减少前置步骤，尽量拆分用例；前置数据尽量采用数据库造数；牺牲执行时间，换取稳定性；
2. 元素定位准确度，可能用的是vue框架，很多元素没有id或者name，只能通过css或者xpath去定位，一但开发修改页面层级会很尴尬