# # A recursive solution for subset sum 
# # problem 

# def is_subset_sum(set, n, sum):
#     # base class 
#     if sum == 0:
#         return True
#     if n == 0:
#         return False
    
#     # if last element is greater than 
#     # sum, then ignore it 
#     if set[n-1] > sum:
#         return is_subset_sum(set , n-1, sum)
    
#     # else, check if sum can be obtained
#     # by any of the following
#     # (a) including the last element 
#     # (b) excluding the last element 
#     return is_subset_sum(set, n-1, sum) or is_subset_sum(set, n-1, sum-set[n-1])

# # Driver code 
# if __name__ == '__main__':
#     set = [3, 34,4,12,5,2]
#     sum = 9
#     n = len(set)
#     if is_subset_sum(set, n, sum) == True:
#         print("Found a subset with given sum")
#     else:
#         print("No subset with given sum")




# by using dynamic approach 


# def is_subset_sum(set, n, sum):
#     # the value of subset[i][j] will be 
#     # true if there is a 
#     # subset of set[0..j-1] with sum equal to i 
#     subset = ([False for i in range(sum+1)] for i in range(n+1))

#     # if sum is 0, then answer is true 
#     for i in range(n+1):
#         subset[i][0] = True

#     # if sum is not 0 and set is empty
#     # then answer is false 
#     for i in range(1, sum+1):
#         subset[0][i] = False
    
#     # fill the subset table in bottom up manner 
#     for i in range(1, n+1):
#         for j in range(1, sum+1):
#             if j<set[i-1]:
#                 subset[i][j] = subset[i-1][j]
#             if j>= set[i-1]:
#                 subset[i][j] = (subset[i-1][j] or subset[i-1][j-set[i-1]])
#     return subset[n][sum]

# if __name__ == '__main__':
#     set = [3,34,4,12,5,2]
#     sum = 9
#     n = len(set)
#     if is_subset_sum(set, n, sum) == True:
#         print("Found a subset with given sum")
#     else:
#         print("No subset with given sum")



#Dynamic programming approch for sum of subset

def isSubsetSum(set,n,sum):
    # the value of subset[i][j] will be 
    # true if there is a 
    # subset of set[0..j-1] with sum equal to i 
    subset =([[False for i in range(sum+1)] for i in range(n+1)])


    # if sum is 0, then answer is true 
    for i in range(n+1):
        subset[i][0]=True

    # if sum is not 0 and set is empty
    # then answer is false 
    for i in range(1,sum+1):
        subset[0][i]= False

    # fill the subset table in bottom up manner 
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if j < set[i-1] :
                subset[i][j] = subset[i-1][j]
            if j >= set[i-1]:
                subset[i][j] =(subset[i-1][j] or subset[i-1][j- set[i-1]])
    return subset[n][sum]

if __name__ == '__main__' :
    set =[3,34,4,12,5,2]
    sum = 9
    n= len(set)
    if (isSubsetSum(set,n,sum) == True) :
        print("Found a subset with given sum")
    else:
        print("No subset with given sum")