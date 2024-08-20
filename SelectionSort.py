A = [1,-10,0,4,2,8,-3,5]
n = len(A)
for i in range(n-1):
    min_index = A.index(min(A[i+1:n]))
    
    if A[i]>A[min_index]:
        A[i],A[min_index] = A[min_index],A[i]
   
    print(A)
