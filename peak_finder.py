# Problem: Find the peak if it exists

input1 = [1,4,3] #should return the peak #4
input2 = [2,2,3] #should return none

def find_peak(lst):
    '''Finds a peak of an arr if it exists'''

    # print('Masha')

    peak_num=None
    end_lst = len(lst)-1

    for i in range(len(lst)):
        if i == 0:
            if lst[i] >= lst[i+1]:
                peak_num = lst[i]

        elif i == end_lst:
            if lst[i] >= lst[i-1]:
                peak_num = lst[i]

        elif (lst[i] >= lst[i-1]) and (lst[i] >= lst[i+1]):
            peak_num=lst[i]
        
        else:
            return None

    return peak_num



print(find_peak(input1))
print(find_peak(input2))