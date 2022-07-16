import pymysql as pymysql

from config.RunConfig import RunConfig


# mysql 连接工具
class MysqlToolBase:
    # 初始化 mysql 连接
    def __init__(self):
        # mysql_ip
        self.host = RunConfig().mysql_ip
        # mysql_port
        self.port = RunConfig().mysql_port
        # mysql_db
        self.db = RunConfig().db_name
        # mysql_user
        self.user = RunConfig().db_username
        # mysql_pwd
        self.passwd = RunConfig().db_password
        # mysql_charset
        self.charset = RunConfig().mysql_charset
        # mysql 连接
        self.mysql_conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db,
                                          port=self.port, charset=self.charset)

    # execute 任何操作
    def execute(self, sql):
        """
        执行 sql 语句
        :param sql: sql 语句
        :return: select 语句返回
        """
        # 从 mysql 连接中获取一个游标对象
        cursor = self.mysql_conn.cursor()
        # sql 语句执行返回值
        ret = None
        try:
            # 执行 sql 语句
            ret = cursor.execute(sql)
            # 提交
            self.mysql_conn.commit()
        except Exception as e:
            # 异常回滚数据
            self.mysql_conn.rollback()
        # 关闭游标
        cursor.close()
        # 返回
        return format(ret)

    # 获取 mysql 连接
    def get_mysql_conn(self):
        return self.mysql_conn

    # mysql 连接释放
    def release_mysql_conn(self):
        if self.mysql_conn is not None:
            self.mysql_conn.close()
            self.mysql_conn = None