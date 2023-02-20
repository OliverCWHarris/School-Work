stacka=[]
array1=[26,13,9,427]
def push(stack, thing):
    stack.append(thing)

def pop(stack):
    return stack.pop()

push(stacka, 31)
pop(stacka)
push(stacka, 26)
push(stacka, array1)
pop(stacka)
push(stacka, 'cheese')
print(pop(stacka))