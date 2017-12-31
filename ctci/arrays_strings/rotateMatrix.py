''' Rotate NxN matrix by 90 degrees and in-place'''

def rotateMatrix(a):
    layers=len(a)
    for i in range(int((layers)/2)):
        for j in range(i,layers-i-1):
            tmp=a[i][j]                                 #temp=top
            a[i][j]=a[layers-j-1][i]                    #top=left
            a[layers-j-1][i]=a[layers-1-i][layers-j-1]  #left=bottom
            a[layers-1-i][layers-j-1]=a[j][layers-1-i]  #bottom=right
            a[j][layers-1-i]=tmp                        #right=temp     
    return a
    

a= [[1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]]
    
print(rotateMatrix(a))