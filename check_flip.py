def check_de_flip_c(L_cycle):
    for idx, ver in enumerate(L_cycle):
        ver_after_0 = '0' + ver[:-1]
        ver_after_1 = '1' + ver[:-1]
        if ver_after_0 != L_cycle[idx-1] and ver_after_1 != L_cycle[idx-1]:
            print('\tNO. because {0} and {1} with index is {2},{3} index'.format(L_cycle[idx-1],ver,idx-1,idx))
            return False

    for idx, ver in enumerate(L_cycle[:-1]):
        if ver in L_cycle[idx+1:] or ver[::-1] in L_cycle[idx+1]:
            print('\tNo. because {0} with index is {1}'.format(ver,idx))
            return False
    return True
        
    
def check_de_flip(filename):
    """ return bool List like as [True,False,...] whether it is de bjuin cycle or not.

        It is that check the line in file is string with de bjuin flip cycle.

        Examples
        --------
        The file form following;
            010 101
            010 111
            00100 01000 10001 00011 00110 01101 11011 10111 01110 11100 11001 10010
            ...

        >>> check_de_flip(f_name)
        Let's ....
        ...
        ...
        ...
        [True,False,True,....]
        
    """
    L_result = []
    print('Let\'s check that it is de bujin flipping cycle.')
    
    with open(f_name) as f:
        for fidx,line in enumerate(f):
            L_result.append(False)
            check_de = True
            
            
            de_flip_cycle = line.split()
            print('----------------------------------------------------------------')
            print('\nfidx : {0}, cycle : {1}'.format(fidx,line))
            
            # check that it is de bujin cycle?
            print('Is it de_cycle? ', end ='')
            for idx, ver in enumerate(de_flip_cycle):
                ver_after_0 = '0' + ver[:-1]
                ver_after_1 = '1' + ver[:-1]

                if ver_after_0 != de_flip_cycle[idx-1] and ver_after_1 != de_flip_cycle[idx-1]:
                    print('\tNO. because {0} and {1} with index is {2},{3} index'.format(de_flip_cycle[idx-1],ver,idx-1,idx))
                    check_de = False
                    break
            if check_de == False:
                continue
            
            print('\tYES')

            # check that it is flipping cycle?
            print('Is it flipping cycle? ', end ='')
            for idx, ver in enumerate(de_flip_cycle[:-1]):
                if ver in de_flip_cycle[idx+1:] or ver[::-1] in de_flip_cycle[idx+1]:
                    print('\tNo. because {0} with index is {1}'.format(ver,idx))
                    check_de = False
                    break
            if check_de == False:
                continue
            print('\tYES. It\'s de bujin cycle with flipping!')
            L_result[-1] = True
    print('----------------------------------------------------------------')
    return L_result

# 예제
print('예제1) 실행안되면 파일경로를 바꾸세요')
print('f_name = \'C:/Users/clean/Desktop/check_de_flip.txt\'')
print("""with open(f_name,\'w\') as f:
    f.write('00100 01000 10001 00011 00110 01101 11011 10111 01110 11100 11001 10010' + '\\n')
    f.write('00100 01000 10001 00011 00110 01101 11011 10111 01110 11100 11011 10010' + '\\n')""")
print('check_de_flip(f_name)')
print('')

##f_name = 'C:/Users/clean/Desktop/check_de_flip.txt'
##
##with open(f_name,'w') as f:
##    f.write('00100 01000 10001 00011 00110 01101 11011 10111 01110 11100 11001 10010' + '\n')
##    f.write('00100 01000 10001 00011 00110 01101 11011 10111 01110 11100 11011 10010' + '\n')
##
##check_de_flip(f_name)
