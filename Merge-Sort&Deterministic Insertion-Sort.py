import timeit,csv,random

def merge(arr,l,r):
    if r-l>1:
        mid=(l+r)//2
        merge(arr,l,mid)
        merge(arr,mid,r)
        mergesort(arr,l,mid,r)


def mergesort(arr,l,m,r):
    left=arr[l:m]
    right=arr[m:r]

    i=0
    j=0
    k=l

    while(l+i <m and m+j <r):
        if (left[i] <= right [j]):
            arr[k]=left[i]
            i+=1

        else:
            arr[k]=right[j]
            j+=1
        k+=1

    if l+i <m :
        while k< r:
            arr[k] =left[i]
            i+=1
            k+=1
    else:
        while k<r:
            arr[k]=right[j]
            j+=1
            k+=1
##arr=[1,5,987,675,10012132,789,2,8,5,3]
##merge(arr,0,len(arr))
##print(arr)

def fileinput():
    file=open("input.txt" ,"r")
    content=file.readlines()
    arr=[int(i) for i in content]
    file.close()
    return arr


#Question 2
#partiton incomplete
'''
def partition(arr,l,r,x):
    i=l-1
    for j in range(l,r-1):
        if arr[j]<=x:
            i+=1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    tempe=arr[i+1]
    arr[i+1]=arr[r-1]
    arr[r-1]=tempe

    return i+1
    '''

def insertionsort(arr):
    for i in range(1, len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key< arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
def select(arr,l,r,i):
#1. Divide the n elements of the input array into [n/5]
    array=arr[:]
    five_lists=[array[i*5:(i+1)*5] for i in range((len(array)+4)//5)]
#2.Find the median of each of the [n/5]
    medians=[]
    for i in five_lists:
        #insertion sort the small array instead of entire array
        srt=insertionsort(i)
        medians.append(srt[int((len(srt)-1)/2)])

#3.Use select recursively to find the median x of the [n/5]
    if len(medians)==1:
        top_median=medians[0]
        print("Median of median is",top_median)
    else:
        top_median=select(medians,0,len(medians),(int((len(medians)-1)/2)))
    
#4.Partition the input array around the median-of-median x using modified partition
    #step 4 not fully implemented
    #position=partition(arr,0,len(arr),top_median)
    #print(position)
#5.If i==k return x else use select recursively to find the ith smallest element
#arr=random.sample(range(1,101),90)
#select(arr,0,len(arr),1)

#main
run_median=[]
run_merge=[]
size=5000
for i in range(20):
    arr=fileinput()
    arr=arr[:size]
    test_merge="merge(arr,0,len(arr))"
    test_select="select(arr,0,len(arr),1)"
    time_select=timeit.timeit(stmt=test_select,globals=globals(),number=1)
    time_merge=timeit.timeit(stmt=test_merge,globals=globals(),number=3)
    avg_merge=round(time_merge/3,8)
    run_median.append([size,time_select])
    run_merge.append([size,avg_merge])
    print("Current input size is", size,"Average input time is", avg_merge)
    print("time for select median",time_select)
    size+=5000

print("sample output of first 500 elements")
print(arr[:500])

#output results
#commented out for sanitary purpose
'''
with open("pa3_plot.csv", "w",newline='') as result:
    wr=csv.writer(result, quoting=csv.QUOTE_ALL)
    for i in run_merge:
        wr.writerow(i)
    for j in run_median:
        wr.writerow(j)
'''

