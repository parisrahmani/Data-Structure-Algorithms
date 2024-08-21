#Bubble_Sort

A = [1,-10,0,4,2,8,-3,5]

n = len(A)
j = 0

for i in range (n-1):
    for j in range(n-1,i,-1):
        if A[j]<A[j-1]:
            A[j],A[j-1] = A[j-1],A[j]
        
print(A)
    
