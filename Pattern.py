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

    
    #----------------------------------------------------

n=int(input("enter the number "))

for i in range(n):
    print("*",end=" ")

                                                        * * * * * * 

------------------*********------------------
n=int(input("Enter the number :"))

for i in range(n):
    print((str(n)+" ")*n)


                                                       6 6 6 6 6 6 
                                                       6 6 6 6 6 6 
                                                       6 6 6 6 6 6 
                                                       6 6 6 6 6 6 
                                                       6 6 6 6 6 6 
                                                       6 6 6 6 6 6 


-----------------*******--------------------------------------

n = int(input("Enter no of row: "))               # The no of space every row : n-i-1
for i in range(n):                                # Which symbol : i+1
     print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))      # How many times : i+1


                                                    # Output
                                                    #     1
                                                    #    2 2
                                                    #   3 3 3
                                                    #  4 4 4 4
                                                    # 5 5 5 5 5


#--------------------------------------------------------
 n = int(input("Enter no of row: "))  
 for i in range(7):
    for j in range(5):
         print("*",end="")
     print()
                                                      # Output

                                                      # *****
                                                      # *****
                                                      # *****
                                                      # *****
                                                      # *****
                                                      # *****
                                                      # *****
                                                      
#--------------------------------------------------------
n = int(input("Enter no of row: "))  
for row in range(7):
    for col in range(5):
        if(row==0 or row==6):
            print('*',end=" ")
        elif(row in{1,2,3,4,5} and (col in {0,4})):
            print('*', end=" ")

        else:
            print(' ',end=' ')
    print()

                                                            # Output

                                                            # * * * * *
                                                            # *       *
                                                            # *       *
                                                            # *       *
                                                            # *       *
                                                            # *       *
                                                            # * * * * *
                                        
                                        
 ----------------------------*********---------------------


n = eval(input("enter 1st fractional number")) # 1/4
m = eval(input("enter 2nd fractional number")) # 1/2

def fraction(a,b):



    return a+b+10



print(fraction(n,m))

-------------*******------------------------


n = int(input("enter the row number: "))

for i in range(n):
    print((n-i-1)*" ",end=" ")
    for j in range(i+1):
        print(chr(64+n-j),end=" ")

    print()
                                                      I 
                                                     I H 
                                                    I H G 
                                                   I H G F 
                                                  I H G F E 
                                                 I H G F E D 
                                                I H G F E D C 
                                               I H G F E D C B 
                                              I H G F E D C B A 
                                             
                                             
 -----------------------**********---------------------------------
