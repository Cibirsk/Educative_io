arr = [9, 8, 1, 8, 1, 7]
targetNumber = 1
currentIndex = 0

"""
def findNumb(arr,targetNumber,currentIndex):
    if targetNumber not in arr[currentIndex]:
        return -1
"""    

def findNumbIte(arr,targetNumber,currentIndex):
    for i in arr:
        if arr[i]== targetNumber:
            return i
        else:
            return -1

print(findNumbIte(arr,targetNumber,currentIndex))
