import yaml
from config.logger import logger


def loadyaml(file_path,part):
    try:
        datafile = open(file_path, 'r', encoding='utf-8')
        data = yaml.load(datafile, Loader= yaml.FullLoader)
        casedata = data[part]
        return casedata
    except:
        logger().error("读取用例文件异常,请检查yaml" )

