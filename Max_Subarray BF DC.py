import timeit
import csv
#bruteforce
"""Because the brute force takes really long time, I will just print
results when timeit function invokes bruteforce instead of return.
Output looks bit messy"""


"""input size of 5000 just takes way too much time, so I downsized it to 2000
with increment of 400, but even that took too long. So I just used 100 with
increment of 200"""
def bruteforce(arr):
    maxsum=-9999
    result=[]
    current_sum=0
    lind=0
    rind=0

    for i in range(len(arr)+1):
        for j in range(len(arr)+1):
            if arr[i:j]:
                current_sum=sum(arr[i:j])
                if current_sum>maxsum:
                    maxsum=current_sum
                    result.append((i,j))
    print (result[-1],maxsum,"--BruteForce--Results")
                
#divideconquer
def max_subarray(alist, start, end):
    # base case
    if start == end - 1:
        return start, end, alist[start]
    else:
        mid = (start + end)//2
        lstart, lend, lmax = max_subarray(alist, start, mid)
        rstart, rend, rmax = max_subarray(alist, mid, end)
        cstart, cend, cmax = max_mid_subarray(alist, start, mid, end)
        if (lmax > rmax and lmax > cmax):
            return lstart, lend, lmax
        elif (rmax > lmax and rmax > cmax):
            return rstart, rend, rmax
        else:
            return cstart, cend, cmax
 
def max_mid_subarray(alist, start, mid, end):
    sum_l = -999
    sum_temp = 0
    cstart = mid
    for i in range(mid - 1, start - 1, -1):
        sum_temp = sum_temp + alist[i]
        if sum_temp > sum_l:
            sum_l= sum_temp
            cstart = i
 
    sum_r = -999
    sum_temp = 0
    cend = mid + 1
    for i in range(mid, end):
        sum_temp = sum_temp + alist[i]
        if sum_temp > sum_r:
            sum_r = sum_temp
            cend = i + 1
    return cstart, cend, sum_l + sum_r

#read text file
def fileopen():
    file=open("input.txt","r")
    content=file.readlines()
    arr=[int(i) for i in content]
    file.close()
    return arr

#main_code
run_time_brute=[]
run_time_dc=[]
size=100
for i in range(20):
    arr=fileopen()
    arr1=arr[:size]

    test_brute="bruteforce(arr1)"
    test_dc="max_subarray(arr1,0,len(arr1))"
    time_brute=timeit.timeit(stmt=test_brute,globals=globals(),number=3)

    time_dc=timeit.timeit(stmt=test_dc,globals=globals(),number=3)
    avg_brute=round(time_brute/3,8)
    run_time_brute.append([size,avg_brute])
    avg_dc=round(time_dc/3,8)
    run_time_dc.append([size,avg_dc])
    


    print("----BruteForce--Current_list_input:",size,"|Average run time: ",avg_brute)
    print("----Divide&Conqure--Current_list_input:",size,"|Average run time is:",avg_dc)
    #position,maxsum=bruteforce(arr1)
    #print(position[0],position[1],maxsum)
    lo,hi,tsum=max_subarray(arr1,0,len(arr1))
    print(lo,hi,tsum,"Divide&Conquer--Results")
    print()
    size+=200

#output file

with open("pa2_test.csv", 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for i in run_time_brute:
         wr.writerow(i)
     for j in run_time_dc:
         wr.writerow(j)
         
