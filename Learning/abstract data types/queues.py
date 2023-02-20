queue=[]

def enqueue(thing):
    global queue
    queue.append(thing)
    if len(queue)>3:
        queue=queue[:3]

def dequeue():
    global queue
    queue.remove[0]

def empty():
    global queue
    if len(queue)==0:
        return True
    else:
        return False

def full():
    global queue
    if len(queue)==3:
        return True
    else:
        return False


enqueue('cheese')
print(queue)
print(empty())
print(full())
enqueue(13)
enqueue(17.4)
print(queue)
enqueue('rats')
print(empty())
print(full())