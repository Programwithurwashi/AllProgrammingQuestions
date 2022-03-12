#WAP to find the time currnttime year month and localtime
import time
epc=time.time()
print(epc)
localtime=time.localtime(epc)
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(time.ctime(epc))