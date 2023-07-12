def max_min(A):
    maxi=float('-inf')
    mini=float('inf')
    for i in range(len(A)):
        if A[i]>maxi:
            maxi=A[i]
        if A[i]<mini:
            mini=A[i]
    return maxi+mini

A=list(map(int,input("Enter the Array Elements: ").split()))
print(max_min(A))