def search(mat,value):
    i=0
    n=len(mat[0])
    j=n-1
    while(i<n and j>=0 ):
        if(mat[i][j]==value):
            return True
        
        if(mat[i][j]>value):
            j-=1
        else:
            i+=1
    return False

mat = [[10,20,30,40],
       [15,25,37,45],
       [32,35,40,48],
       [37,39,46,50]]
x=55
print(search(mat,x))
