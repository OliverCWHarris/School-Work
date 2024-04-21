import numpy as np
ray1 = (input("Enter a list1 of your choice with commas in between and no spaces: "))
ray2 = (input("Enter a list2 of your choice with commas in between and no spaces: "))
list1 = [int(x) for x in ray1.split(",")]
list2 = [int(x) for x in ray2.split(",")]
vector1 = np.array(list1)
vector2 = np.array(list2)
vector = ''
print(vector1)
print(vector2)