def cyclicRotation(A, K):
    if len(A) == 0:
        return []
    while K > 0:
        A = [A[-1]] + A[0:-1]
        K -= 1
    return A

#print(cyclicRotation([3,8,9,7,6], 3)) 


def oddOccurrencesInArray(A):
    seen = set()
    for i in A:
        if i in seen:
            seen.remove(i)
        else:
            seen.add(i)
    return seen.pop()
    

print(oddOccurrencesInArray([9,3,9,3,9,7,9]))