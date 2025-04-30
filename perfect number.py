#is equal to the numberitself.
n=int(input("enter any number:"))
sum1=0
#loop through all numbers less than 'n' to find divisiors
for i in range(1,n):
    if n% i==0:
        sum1+=i
        #add divisior to sum1
        # check if the sum of divisiors equals the original number
        if sum1==n:
                print("The number is perfect number!")
              else:
                print("The number is not a perfect number!")
