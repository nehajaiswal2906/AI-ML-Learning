# Rotate a list by k positions. 
# Example: [1,2,3,4,5] with k=2 becomes [4,5,1,2,3].


def rotate_list(numbers, k):

    if len(numbers)==0:
        print("The list is Empty. No rotation.")
        return None
    
    else:
        k%=len(numbers)
        last_k_items=[]

        for i in range ((-k),0):
            last_k_items.append(numbers[i])

        for i in range(0,k):
            numbers.pop()

        return last_k_items+numbers

n=int(input("Enter the number of elements:"))
numbers=[]

for i in range (1,n+1):
    numbers.append(int(input(f"Enter element {i}: ")))

k=int(input("Enter the value by which list should be rotated:-"))

rotated_list=rotate_list(numbers,k)

if rotated_list is None:
    pass
else:
    print("The rotated list is:",rotated_list)
