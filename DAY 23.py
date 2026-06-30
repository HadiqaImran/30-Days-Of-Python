import numpy as np
a = np.arange(1, 25)
print(a)
b=a.reshape(2,12)
print(b)
sub_matrix = b[:, 2:4]  
print(sub_matrix)
matrix=np.hsplit(b,(3,4))
print(matrix)