# # código python a continuación!
# arr = [1,3,5,7]
# arr[0], arr[1] = arr[1], arr[0]

# Python3 program to swap elements
# at given positions

# Swap function
def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1-1, pos2-1))
