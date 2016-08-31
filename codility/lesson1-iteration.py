def binarygap(N):
    result = 0
    counter = 0
    isOne = False
    while N > 0:
        if N % 2 == 0 and isOne:
            counter += 1
        elif N % 2 == 1:
            if isOne:
                result = max(result, counter)
            isOne = True
            counter = 0
        N >>= 1
    return result 

print(solution(1041))
