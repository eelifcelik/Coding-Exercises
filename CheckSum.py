"""This function takes a list and an integer as input and returns True if the sum of any two numbers in the list
is equal to num.If no such pair exists, return False.
"""

def check_sum(num_list, num):
     n=len(num_list)
     for i in range(n):
         for j in range(n-1):
            if(num_list[i]+num_list[j]==num):
             print("True")
             return True
     else:
       print("True")
       return False

#Testing the function
list_1= [9, -3, 7, 11, 5]
check_sum(list_1, 2)
