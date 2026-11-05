
# Given a list, print the second largest number.

def second_largest_number(numlist):

    numlist=list(set(numlist))
    numlist.sort()

    if len(numlist)==1:
        print("There is only a single unique element. So, No second largest.")
        return None

    elif len(numlist)==0:
        print("There are no elements in the list. So,No second largest.")
        return None
    
    else:

        largest=numlist[0]
        second_largest=numlist[0]

        for number in numlist:

            if number>largest:
                second_largest=largest
                largest=number

            elif number>second_largest:
                second_largest=number

        return second_largest

n=int(input("Enter the number of elements:"))
numlist=[]

for i in range (1,n+1):
    numlist.append(int(input(f"Enter element {i}: ")))

second_largest=second_largest_number(numlist)

if second_largest is None:
    pass
else:
    print("The second largest number is:",second_largest)
