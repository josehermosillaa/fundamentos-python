x = [1,5,3,2,0,8,4,5,67,8,9,90,1]

def bubbleSort(arr):
    count = 0
    for j in range(len(arr)-1):
        # print(f'\n\n ------> iteracion {j}')
        for i in range(len(arr)-1-j):
            count +=1
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    # print(f'# de evaluaciones {count}')
    return arr
        
print(bubbleSort(x))