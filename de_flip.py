import shutil

def de_flip(n):
    """ n is odd
        start is start string with center is 1. otherwise 0. (ex 00100)
        
    """
    start = '0'*(n//2) + '1' + '0'*(n//2)
    L = [[start]]
    L_tmp = []
    collect = []

    
    print(L)

    length = 1
    
    while(True):
        flag_cycle = -1
        count = 0
        for next_list in L:
            next_0 = next_list[-1][1:] + '0'
            next_1 = next_list[-1][1:] + '1'
            # 마지막 문자에서 0과 1을 추가한다.

            # 사이클완성!
            if next_0 == start:
                collect.append(next_list)
                flag_cycle = len(next_list)
                count += 1
                continue

            # 리스트에서 플립핑 검사
            if next_0 not in next_list and next_0[::-1] not in next_list:
                copy = next_list.copy()
                copy.append(next_0)
                L_tmp.append(copy)
                
            if next_1 not in next_list and next_1[::-1] not in next_list:
                copy = next_list.copy()
                copy.append(next_1)
                L_tmp.append(copy)
                
        if len(L_tmp) == 0:
            break
        L = L_tmp.copy()
        L_tmp = []

        print("length : {0}, flag_cycle : {1}, count : {2}".format(length,flag_cycle,count))
        length += 1
        
    return collect

def de_flip2(n = 3,start = None):
    """ n is odd
        start is start string with center is 1. otherwise 0. (ex 00100)
        
    """
    if start == None:
        start = '0'*(n//2) + '1' + '0'*(n//2)
    else:
        n = len(start)
    L = [[start]]
    L_tmp = []
    collect = []

    
    print(L)

    length = 1
    
    while(True):
        flag_cycle = -1
        count = 0
        for next_list in L:
            next_0 = next_list[-1][1:] + '0'
            next_1 = next_list[-1][1:] + '1'
            # 마지막 문자에서 0과 1을 추가한다.

            # 사이클완성!
            if next_0 == start:
                collect.append(next_list)
                flag_cycle = len(next_list)
                count += 1
                continue

            # 리스트에서 플립핑 검사
            if next_0 not in next_list and next_0[::-1] not in next_list:
                copy = next_list.copy()
                copy.append(next_0)
                L_tmp.append(copy)
                
            if next_1 not in next_list and next_1[::-1] not in next_list:
                copy = next_list.copy()
                copy.append(next_1)
                L_tmp.append(copy)
                
        if len(L_tmp) == 0:
            break
        L = L_tmp.copy()
        L_tmp = []

        print("length : {0}, flag_cycle : {1}, count : {2}".format(length,flag_cycle,count))
        length += 1
        
    return collect

def de_flip_file(n):
    """ n is odd
        start is start string with center is 1. otherwise 0. (ex 00100)
        
    """
    start = '0'*(n//2) + '1' + '0'*(n//2) # 00100 if n == 5
    f_name = 'C:/Users/clean/Desktop/dede.txt'
    f_tmp  = 'C:/Users/clean/Desktop/dede2.txt'
    f_result = 'C:/Users/clean/Desktop/de_flip.txt'

    #L = [[start]]
    with open(f_name,'w') as f:
        f.write(start + '\n')

    #L_tmp = []
    with open(f_tmp,'w') as ftmp:
        pass
    
    #collect = []
    with open(f_result,'w') as f_end:
        pass
    
    
    length = 1
    
    while(True):
        count = 0
        check_end = True

        with open(f_name) as f:
            for branch in f:
                L_branch = branch.split()
                next_0 = L_branch[-1][1:] + '0'
                next_1 = L_branch[-1][1:] + '1'

                if next_0 == start:
                    with open(f_result,'a') as f_end:
                        f_end.write(branch)
                    count += 1
                    continue

                if next_0 not in L_branch and next_0[::-1] not in L_branch:
                    check_end = False
                    with open(f_tmp,'a') as ftmp:
                        ftmp.write(branch[:-1] + ' ' + next_0 + '\n')

                if next_1 not in L_branch and next_1[::-1] not in L_branch:
                    check_end = False
                    with open(f_tmp,'a') as ftmp:
                        ftmp.write(branch[:-1] + ' ' + next_1 + '\n')
                        
        if check_end == True:
            break
        
        shutil.copyfile(f_tmp, f_name) # 오른쪽으로 복사

        with open(f_tmp,'w') as ftmp:
            pass

        print("length : {0}, count : {1}".format(length,count))
        length += 1
    return None
