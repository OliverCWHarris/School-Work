import numpy as np


def remove_space(var1):
    var1 = var1.replace(" ","")
    return var1

def turn_to_list(var1):
    var1 = [int(x) for x in var1.split(",")]
    return var1

def turn_to_numpy_array(var1):
    var1 = np.array(var1)
    #var1 = np.array(var1, dtype=float)
    #var1 = var1.flatten()
    return var1

def sum_vectors(v1,v2):
    sum = v1 + v2
    return sum

def sub_vectors(v1,v2):
    sub = v1 - v2
    return sub

def scale_vectors(v1,v2):
    scale=int(input("Enter scaling factor\n>"))
    v1 = v1 * scale
    v2 = v2 * scale
    return v1,v2

def dot_product(v1,v2):
    dot = np.dot(v1,v2)
    return dot


vector1 = input("Enter list of numbers with commas between them and no spaces\n>")
vector2 = input("Enter list of numbers with commas between them and no spaces\n>")

vector1 = remove_space(vector1)
vector2 = remove_space(vector2)

vector1 = turn_to_list(vector1)
vector2 = turn_to_list(vector2)

vector1 = turn_to_numpy_array(vector1)
vector2 = turn_to_numpy_array(vector2)

menu = False
while not menu:
    menu_choice = int(input("0 | quit\n1 | sum vectors\n2 | sub vectors\n3 | scale vectors\n4 | dot product\nEnter operation\n>"))

    if menu_choice == 1:
        print(sum_vectors(vector1,vector2))
    elif menu_choice == 2:
        print(sub_vectors(vector1,vector2))
    elif menu_choice == 3:
        print(scale_vectors(vector1,vector2))
    elif menu_choice == 4:
        print(dot_product(vector1,vector2))