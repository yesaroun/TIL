x = [1,2,3,4,5]
y = x
y[2] = 0
print(x)
print(y)
print(id(x))
print(id(y))
"""
[1, 2, 0, 4, 5]
[1, 2, 0, 4, 5]
4379260096
4379260096
"""

# 리스트 복사 방식
a = [5,6,7,8,0]
b = a.copy()
b[2] = 0
print(a)
print(b)
print(id(a))
print(id(b))
"""
[5, 6, 7, 8, 0]
[5, 6, 0, 8, 0]
4344657664
4344900288
"""

# 중첩 리스트 복사 방식
import copy
c = [[1,2], [3,4,5]]
d = copy.deepcopy(c)
d[0][0] = 0
print(c)
#--> [[1, 2], [3, 4, 5]]
print(d)
#--> [[0, 2], [3, 4, 5]]
