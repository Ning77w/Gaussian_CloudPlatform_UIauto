
from config.RunConfig import RunConfig
import pytest
import os

class START_TEST:
    def init_report(self, Report):
        os.mkdir(Report)


    def run():
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        RunConfig.Report = os.path.join(report_dir, now_time)
        init_report(RunConfig.Report)
        allure_results_path = os.path.join(RunConfig.Report)
        html_report_path = os.path.join(RunConfig.Report)
        pytest.main(['-s', '-v', RunConfig.cases_path,
                     '-n', RunConfig.Thread,
                     '--alluredir', allure_results_path,
                     '--maxfail', RunConfig.max_fail,
                     '--reruns', RunConfig.reruntimes
                     ])
        os.system('allure generate ./allure-results -o' + html_report_path)

if __name__ == '__main__':
    pytest.main(['-s', '-v', './test_suite/eventcenter/test_EventDefinition.py', '--alluredir', './allure-results'])
    os.system('allure generate ./allure-results -o ./reports')
    #START_TEST().run()