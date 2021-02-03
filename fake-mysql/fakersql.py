import re

import pymysql as pymysql
from faker import Faker
from faker.providers import BaseProvider
import random


# 根据sql随机生成一条想要的数据
class sqlProvider(BaseProvider):
    def get_random_data(self, datas):
        return random.choice(datas)


class FakerSql(object):
    """
    config 表示：数据库的链接，格式为：
    config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': '123456',
    'db': 'test'
    }
    sql_path 表示：插入表的ddl
    """

    def __init__(self, *, config, sql_path):
        faker = Faker(locale='zh_CN')
        faker.add_provider(sqlProvider)
        self.faker = faker
        self.db = pymysql.connect(**config)
        self.cursor = self.db.cursor()
        self.ddl = sql_path

    # 查询单条
    def query_one(self, *, query_sql):
        try:
            self.cursor.execute(query_sql)
            result = self.cursor.fetchone()
            return result
        except EnvironmentError as e:
            print("Error: unable to fetch data")

    # 查询多条
    def query_all(self, *, query_sql):
        try:
            self.cursor.execute(query_sql)
            results = self.cursor.fetchall()
            return results
        except EnvironmentError as e:
            print("Error: unable to fetch data", e)

    # 关闭数据库
    def close(self):
        self.db.close()

    # 根据sql文件生成python insert代码
    def generator_insert_python_code(self):
        sql_regex = r'(?<=`).*?(?=`)'
        values = ''
        fileds = ''
        table_name = ''
        with open(self.ddl, encoding='utf-8') as f:
            contents = f.readlines()
            create_content = contents[0]
            field = re.search(sql_regex, create_content)
            try:
                if field is not None:
                    table_name = field.group()
                for content in contents:
                    field = re.search(sql_regex, content)
                    if field is not None and self.check_sql_filed(content):
                        values = values + '%s,'
                        column = '`' + field.group() + '`,'
                        fileds = fileds + column
                fileds = fileds[0:-1]
                values = values[0:-1]
                values = ') values (' + values + ')'
            except ValueError as e:
                print('table ddl error:', e)
        return {
            'insert_sql': 'insert into `' + table_name + '` (' + fileds + values,
            'fields': fileds,
            'table_name': table_name
        }

    @classmethod
    def check_sql_filed(cls, content):
        filed_type = ['tinyint', 'smallint', 'mediumint', 'int', 'bigint', 'float', 'double', 'char', 'varchar',
                      'tinytext', 'text', 'mediumtext', 'longtext', 'decimal',
                      'date', 'time', 'datetime', 'timestamp', 'bit']
        for filed in filed_type:
            if filed in content or filed in str(content).upper():
                return True
        return False


if __name__ == '__main__':
    local_config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': '123456',
        'db': 'test'
    }
    fakerSql = FakerSql(config=local_config, sql_path='table.ddl')
    query_product_sql = "select pid,p_name,price,stock from product"
    products = fakerSql.query_all(query_sql=query_product_sql)
    product = fakerSql.faker.get_random_data(products)
    insert_sql = fakerSql.generator_insert_python_code()['insert_sql']
    fakerSql.cursor.execute(
        insert_sql, ('0', product[0], product[1], product[2], product[3])
    )
    fakerSql.db.commit()
    fakerSql.close()
