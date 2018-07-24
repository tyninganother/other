# encoding: UTF-8

"""
导入MC导出的CSV历史数据到MongoDB中
"""

from vnpy.trader.app.ctaStrategy.ctaBase import TICK_DB_NAME
from vnpy.trader.app.ctaStrategy.ctaHistoryData import loadTbPlusCsv


if __name__ == '__main__':
    #loadTbPlusCsv('IF1801_Tick.csv', TICK_DB_NAME, 'IF1801')
    #loadTbPlusCsv('IF1802_Tick.csv', TICK_DB_NAME, 'IF1802')
    loadTbPlusCsv('T1809_Tick.csv', TICK_DB_NAME, 'T1809')
    #loadTbPlusCsv('rb000_Tick.csv', TICK_DB_NAME, 'rb000')

    #loadMcCsv('rb0000_1min.csv', MINUTE_DB_NAME, 'rb0000')

