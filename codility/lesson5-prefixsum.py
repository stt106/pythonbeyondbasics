def passing_cars(A):
    res = 0
    zeros = 0
    for car in A:
        if car == 0:
            zeros += 1
        else:
            res += zeros
    return (-1 if res > 1000000000 else res) 


'''Count the number divisors between [A, B] of K'''
def counting_div(A, B, K):
    r = B // K - A // K # not the same as (B-A) // K
    return r + (1 if A % K == 0 else 0)

print(counting_div(1,1,11))
print(counting_div(6, 11, 2))
print(counting_div(11, 345, 17))


def GenomicRangeQuery(S, P, Q):
    if len(S) == 0:
        raise ValueError('invalid input of S')
    
    M = len(P)
    if M != len(Q):
        raise ValueError('invalid input of P and Q; they must have the same length')

    res = []    
    #factors = {'A':1, 'C':2, 'G':3, 'T':4}

    """This is a helper function to get a list of seen index of a genomic letter"""
    def get_seen_index(source_list, index_list, letter, index):
        if source_list[index] == letter:
            index_list[index] = index
        elif index > 0:
            index_list[index] = index_list[index-1]
    
    s = len(S)
    seen_index_A = [-1] * s
    seen_index_C = [-1] * s
    seen_index_G = [-1] * s
    seen_index_T = [-1] * s

    for i in range(s):
        get_seen_index(S, seen_index_A, 'A', i)
        get_seen_index(S, seen_index_C, 'C', i)
        get_seen_index(S, seen_index_G, 'G', i)
        get_seen_index(S, seen_index_T, 'T', i)
    
    for j in range(M):
        q = Q[j]
        p = P[j]
        # because it's looking for the minimum factor for each range of [p,q], it can check the seen index list in order of ACGT
        # the key here is changing the search of a min of a range into comparing two indices (seen index of letters for q and p itself)
        if seen_index_A[q] >= p:
            res.append(1)
        elif seen_index_C[q] >= p:
            res.append(2)
        elif seen_index_G[q] >= p:
            res.append(3)
        elif seen_index_T[q] >= p:
            res.append(4)

    return res 

print(GenomicRangeQuery('CAGCCTA', [2, 5, 0], [4, 5, 6]))
    
