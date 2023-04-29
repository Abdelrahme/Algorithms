import queue
#q1=queue.Queue()
""""q1=[]
for i in range(9,-1,-1):
    q1.append(i)
    for i in range(len(q1)):
        for j in range(len(q1)):
            if q1[j]<q1[i]:
                temp=q1[i]
                q1[i]=q1[j]
                q1[j]=temp
while not len(q1)==0:
    print(q1.pop())
"""
class Schedule(object):
    def __init__(self, name, at, bt):
        self.name = name
        self.at = at
        self.bt = bt
        self.ct = 0


 def solution2(processes):
     pro = []
     for p in processes:
        pro.append(Schedule(p[0], p[1], p[2]))
     pro.sort(key=lambda x: x.at)
     pro[0].ct = pro[0].bt + pro[0].at

     for j in range(1, len(processes)):
         ab = pro[j-1].ct

         # partial sorting  <-------------- right here !!!!
         waitings = list(filter(lambda x: x.at <= ab, pro[j:]))
         pro[j:j+len(waitings)] = sorted(waitings, key=lambda x: x.bt)
         # partial sorting end

         if pro[j-1].ct < pro[j].at:
             pro[j].ct = pro[j-1].ct + pro[j].bt + pro[j].at - pro[j-1].ct
         else:
             pro[j].ct = pro[j-1].ct + pro[j].bt

