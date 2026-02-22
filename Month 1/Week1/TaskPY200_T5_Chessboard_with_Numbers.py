n = int(input("Enter N for the chessboard: "))
mat = []



for i in range(1,n+1):
    row = [0 for u in range(n)]
    
    for j in range(1,n+1):
        if i == j :
            row[j-1]="X"

        elif (i+j)%2 == 0:
            row[j-1]=1

        else:
            row[j-1]=0

    mat.append(row)

print(mat)

# print(row)
# row[0]="X"
# row[1]=0
# row[2]=1
# print(row)
# row[0]=0
# row[1]="X"
# row[2]=0
# print(row)
