import datetime

import radar as radar
from faker import Faker


class FakeData(object):
    def __init__(self):
        self.faker = Faker(locale='zh_CN')

    """
    使用说明：构造金额，digits表示几位数子，比如digits=3 表示 100~999 之间数字
    """

    def generator_amt(self, digits=None):
        return self.faker.random_number(digits=digits)

    """
    使用说明：构造地址
    返回示例：
    {'address': '安徽省建军县吉区南昌路N座 878320', 'province': '陕西省', 'city': '乌鲁木齐市', 'street': '何路Z座',
    'street_name': '蔡街', 'company': '襄樊地球村传媒有限公司'}
    """

    def generator_address(self):
        faker = self.faker
        return {
            'address': faker.address(),
            'province': faker.province(),
            'city': faker.city(),
            'street': faker.street_address(),
            'street_name': faker.street_name(),
            'company': faker.company()
        }

    """
    注意事项：参数日期格式是%Y-%m-%d
    返回示例：2019-06-22
    """

    def generator_date(self, start, stop):
        time = radar.random_datetime(
            start=radar.utils.parse(start),
            stop=radar.utils.parse(stop))
        return time

    def generator_time(self, year=2020, *, month):
        time = radar.random_datetime(
            start=datetime.datetime(year=year, month=month, day=1),
            stop=datetime.datetime(year=year, month=month, day=28))
        return time

    """
    指定日期范围：具体到日期之间 比如start_year=2020, end_year=2021, start_month=12, end_month=1, start_date=1,
                                    end_date=15表示2020-12-01~2021-01-15之间日期
    返回示例：2020-12-21 01:10:49
    """

    def generator_date_time(self, start_year=2020, end_year=2020, *, start_month, end_month, start_date, end_date):
        time = radar.random_datetime(
            start=datetime.datetime(year=start_year, month=start_month, day=start_date),
            stop=datetime.datetime(year=end_year, month=end_month, day=end_date))
        return time


if __name__ == '__main__':
    faker = FakeData()
    print(faker.generator_date_time(start_year=2020, end_year=2021, start_month=12, end_month=1, start_date=1,
                                    end_date=15))
