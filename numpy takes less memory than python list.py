#Compare which is best in python list or numpy for memory size
import numpy as np
a=np.array([1,2,3])
a
print(a)
a[0]
a[1]
a[2]

#program by using python list
#import time
#import sys
#b=range(1000)
#print(sys.getsizeof(5)*len(b))

c=np.arange(1000)
#print(c)
print(c.size*c.itemsize)