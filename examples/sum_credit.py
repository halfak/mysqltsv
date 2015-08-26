import datetime
import sys

from mysqltsv import Reader, Writer

sum = 0.0
for row in Reader(sys.stdin, types=[str, str, float]):
	sum += row.credit or 0

writer = Writer(sys.stdout, headers=["date", "total_credit"])
writer.write([datetime.datetime.now().strftime("%Y-%m-%d"), sum])
