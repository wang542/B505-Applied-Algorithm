from collections import defaultdict

#---------FIle-Loading----------#
def file_open(fname):
    file=open(fname,"r")
    content=file.read()
    tcontent=content.split("\n")
    return tcontent


def graphpart(ls):
#---------Loading Adjacency list and visit tracker---#
    graphdict=defaultdict(list)
    visited={}
    for i in ls[1:]:
        visited[int(i[1])]=False
        visited[int(i[3])]=False
        graphdict[int(i[1])].append(int(i[3]))
        graphdict[int(i[3])].append(int(i[1]))       
#---------Init Necessary variables and construct Queue------#
    start=1
    queue=[]
    part1=[]
    part2=[]
    queue.append(start)
    visited[start]=True
    part1.append(start)
    error="This graph is not bipartite"
#--------------BFS Structure----------------------------------#
    while len(queue)>0:
        s=queue.pop(0)
        for i in graphdict[s]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True
                if s in part1:
                    part2.append(i)
                elif s in part2:
                    part1.append(i)
            if i in part1 and s in part1:
                return error
                break
            elif i in part2 and s in part2:
                return error
                break

    success="This graph is bipartite"
    success+="Partition 1 is :"+str(part1)
    success+=". Partition 2 is :"+str(part2)
    return success
        
#-------------Main-------------------#
p1=file_open("bipartite.txt")
p2=file_open("bipartite2.txt")
p3=file_open("not_bipartite.txt")
p4=file_open("not_bipartite2.txt")
print(graphpart(p1))
print(graphpart(p2))
print(graphpart(p3))
print(graphpart(p4))
