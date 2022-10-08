# Name: Ahmad Alqattan      ID:2192131011

def find_pairs(arr, num):
    returned = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == num:
                returned.append([arr[i], arr[j]])
    return returned

# print(find_pairs([1,2,3,4,5], 9))
# print(find_pairs([9,9,8,4], 13))
#
# [[4, 5]]
# [[9, 4], [9, 4]]