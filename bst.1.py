def binary_search(arr,target):
    #calculate start,end mid values:
    start =0
    end=len(arr) -1
    mid = (start +end) //2 # important
    # while loop:
    while(start<=end):

        if(arr[mid]==target):
        return mid
        elif(target>arr[mid]):
        start = mid +1
        else:
        end = mid -1
        mid =(start+end)//2
return -1  #if not found return -1

arr=[4,5,6,7,8,9,10,11,12]
target=7
result=binary_search(arr,target)
print(result)


    
