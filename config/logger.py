import logging, os,time
from config import RunConfig

def logger():
    logger=logging.getLogger("logger")
    logger.setLevel(logging.DEBUG) #全局日志等级
    # 避免日志重复输出
    if not logger.handlers:
        # 日志路径位置
        log_name=f'{time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())}.log'
        log_path =os.path.join(RunConfig.logs_dir,log_name)

        # 创建handler
        fh=logging.FileHandler(log_path,'a',encoding="utf-8")
        fh.setLevel(logging.DEBUG)

        # 控制台输出日志
        consle=logging.StreamHandler()
        consle.setLevel(logging.DEBUG)
        logger.addHandler(consle)

        #定义handler的输出格式
        formatter=logging.Formatter(fmt="%(asctime)s [%(levelname)s] [%(filename)s](L:%(lineno)s):%(message)s",datefmt="%Y/%m/%d/%X")
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        consle.setFormatter(formatter)
        logger.addHandler(consle)
    return logger