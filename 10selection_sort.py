
arr = [1,4,5,3,2,7,6,9,8,0]

def selectionSort(arr):
    menor = 0
    for j in range(0,len(arr)):
        for i in range(len(arr)-1-j,j,-1 ):
                if i == 0:
                    menor = arr[0]
                elif arr[i]<menor:
                    menor = arr[i]
                    # print(menor)
        arr[j],menor = menor, arr[j]
    return arr

print(selectionSort(arr))