# coding:utf-8
import os
import datetime

__all__ = ["IP", "KEY", "DATA", "LICENSEFILE"]

IP = ""                       # 指定网卡ip, 若不提供, 会自动联网查找
KEY = 'nX4rAqc9mi81Duog5UMbfVI0v3YPOkdZ'
LICENSEFILE = os.path.join(os.path.dirname(__file__), 'license.lic')


DATA = {
    'name': 'yodeng',
    'life_time': True,            # True表示终生有效，False设置开始结束时间
    'start_date': '2021-4-22',    # 开始时间
    'end_date': '2021-4-22',      # 结束时间
    'create_date': datetime.datetime.now().strftime('%Y-%m-%d'),  # 生成时间
}
