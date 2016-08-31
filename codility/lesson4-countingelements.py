def check_permutation(A):
    inputset = set(A)
    for i in range(1, len(A) + 1):
        if i not in inputset:
            return 0
    return 1

def missing_integer(A):
    s = set(A)
    res = 1
    while True:
        if res not in s:
            return res
        else:
            res += 1

#print(missing_integer([1, 3, 6, 4, 1, 2]))


def frogriverone(X, A):
    s = set(range(1, X + 1))
    for i in xrange(len(A)):
        a = A[i]
        if a in s:
            s.remove(a)
        if len(s) == 0:
            return i
    return -1


def maxcounter(N, A):
    res = [0] * N
    currentmax = 0
    for i in A:
        if i >=1 and i <= N:
            res[i-1] += 1
            currentmax = max(currentmax, res[i-1])
        elif i == N + 1:
            res = [currentmax] * N
    return res

print(maxcounter(5, [3,4, 4, 6, 1, 4, 4])) 