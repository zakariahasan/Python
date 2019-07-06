# Printing Number in Right Triangle Shape
n = int(input("enter the number of rows: "))
for i in range (1,n+1): #for row, n+1= to match output to input
    for j in range (1,i+1): # for column
        print(j,end="") # change to "i" to get output 1 22 333
    print()   # new row




# printing Number in pyramid

num = int(input("enter the number of rows:"))

for i in range (1,num+1) :
    for j in range (1,num-i+1) :
        print(" ",end="")

    for j in range (i,0,-1):
        print(j,end='')

    for j in range(2,i+1):
        print(j,end="")
    print()
