A = [1,-10,0,4,2,8,-3,5]

def mergesort(A):
    
    n = len(A)  
    if n < 2:
        return A
        
    mid = n //2
    B = A[:mid]
    C = A[mid:]
    
    B = mergesort(B)
    C = mergesort(C)
    
    i = j = 0
    A = []
    
    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            A += [B[i]]
            i +=1
        else:
            A += [C[j]]
            j += 1
            
    A += B[i:] + C[j:]
    
    return A
    
print(mergesort(A))
    
    
