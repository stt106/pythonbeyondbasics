
import math
def tape_equilibrium(A):
    result = math.inf
    totalsum = sum(A)
    localsum = A[0]
    for i in range(1, len(A)):
        diff = abs(localsum * 2 - totalsum)
        result = min(result, diff)
        localsum += A[i]
    return result


def frogjum(X, Y, D):
    # note that 3/2 returns 1 in Python 2
    return int(math.ceil((Y - X) /D))

print(frogjum(10, 85, 30))


def permmissingele(A):
    range_set = set(range(1,len(A)+2))
    test_test = set(A)
    res = range_set.difference(A)
    return res.pop()

print(permmissingele([2,1,3,5]))
