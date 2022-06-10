from array  import *
import numpy as np
twodarray=np.array([[1,2,3,4],[5,6,7,8],[3,4,57,7],[13,13,13,13]])
new2darray=np.insert(twodarray,0,[[23,45,76,89]],axis=1)
print(new2darray)
sum=1
for i in range(0,len(new2darray)):
    sum=sum*new2darray[i]
print(sum)