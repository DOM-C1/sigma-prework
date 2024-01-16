def maxmin(lst):
    n=1
    max_num=lst[0]
    min_num=lst[0]
    while n <= len(lst)-1:
    
        if lst[n] <= min_num:
            min_num = lst[n]
        if lst[n] >= max_num:
            max_num = lst[n]
        n+=1
    return([min_num,max_num])
