A = [11,28,49,4,81,10,8, 34,23,30,25,8,46]


def BubbleSort(A):
    n = len(A)
    j = 0
    for i in range (n-1):
        for j in range(n-1,i,-1):
            if A[j]<A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]
    return A

def BucketSort(A):
    
    B = [[] for i in range(10)]
    for i in A:
        B[i//10] += [i]
    A = []
    for i in range(10):
        A += BubbleSort(B[i])
    return(A)

BucketSort(A)
    
