import queue
q1=queue.Queue()
for i in range(10):
    q1.put(i)
while not q1.empty():
    print(q1.get())