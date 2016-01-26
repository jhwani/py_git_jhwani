import os
import itertools
import scipy.misc as sc

import json

def draw_G(m):
    import networkx as nx
    import matplotlib.pyplot as plt
    import itertools

    elist = []
    for i,j in itertools.combinations(range(len(m)),2):
        if m[i][j] == 1:
            elist.append((i,j))

    for i in range(len(m)):
        elist.append((i,i))

    G = nx.Graph(elist)
    pos = nx.spring_layout(G)
    nx.draw_networkx(G,pos)
    
    plt.axis('off')
    plt.show()

def mat_data(data):
    if isinstance(data,str):
        if(os.path.exists(data)):
            return mat_file(data)
        else:
            return mat_strdata(data)
    elif isinstance(data,list):
        if isinstance(data[0],list):
            return data
        elif isinstance(data[0],str):
            str_data = ''
            for d in data:
                str_data += d + ' '
            return mat_strdata(str_data)
        else:
            raise TypeError("Unknown type '{0}' for matrix form or filename".format(type(data)))            
    else:
        raise TypeError("Unknown type '{0}' for matrix form or filename".format(type(data)))
    

def mat_strdata(strdata):
    if(not isinstance(strdata,str)):
        raise TypeError("Given data type is {0}. But shoud be data type is {1}".format(type(strdata),str))
        
    data_s = strdata.split()
    mat = []

    for ds in data_s:
        mat.append( [int(d) for d in ds] )

    return mat

def mat_file(filename):
    """
    data type1: json data and list
    data type2: json data and string
    data type3: jsut data and string

    example)
        type1 : [[0,1,1],[1,0,1],[1,1,0]
        type2 : "011\n101\n110\n"
        type3 : 011
                101
                110

    """
    if(os.path.exists(filename) == False):
        print("This filename dose not exists. You should enter exact form as like '/script/test.txt'")
        raise NameError("filename '{0}' is not defined".format(filename))


    import json
    
    with open(filename) as f:
        data_raw = f.readline()
        try:
            data_json = json.loads(data_raw)
            if isinstance(data_json, list):
                return data_json
            elif isinstance(data_json, str):
                return mat_strdata(data_json)
            else:
                raise TypeError("Unknown type '{0}' for matrix form".format(type(data)))
        except:
            mat = []
            mat.append( [int(d) for d in data_raw if d != '\n'] )
            for data_raw in f:
                mat.append( [int(d) for d in data_raw if d != '\n'] )
            return mat

def r(s,t,data):
    mat = mat_data(data)
    n = len(mat)

    ks_edge = sc.comb(s,2,exact=True)

    com_vertice_list = [[ ], [ ]]

    print('begin seek the k{0} in G'.format(s))
    for vertice_set in itertools.combinations(range(n),s):
        e_count = 0
        for i,j in itertools.combinations(vertice_set,2):
            e_count += mat[i][j]
        if(e_count == ks_edge):
            com_vertice_list[0].append(vertice_set)
            print('Find k{0} in G and {1}'.format(s,vertice_set))
            break

    # Find kt in G_bar
    print('begin seek the k{0} in G_bar'.format(t))
    for vertice_set in itertools.combinations(range(n),t):
        e_count = 0
        for i,j in itertools.combinations(vertice_set,2):
            e_count += mat[i][j]
        if(e_count == 0):
            com_vertice_list[1].append(vertice_set)
            print('Find k{0} in G_bar and {1}'.format(t,vertice_set))
            break

    return com_vertice_list

def r_count(s,t,data):
    # find k_s in data
    mat = mat_data(data)
    n = len(mat)

    ks_count = 0
    kt_count = 0
    ks_edge  = sc.comb(s,2, exact=True)
#    kt_edge  = sc.comb(t,2, exact=True)

    com_vertice_list = [[ ], [ ]]

    # Find ks in G
    print('begin seek the k{0} in G'.format(s))
    for vertice_set in itertools.combinations(range(n),s):
        e_count = 0
        for i,j in itertools.combinations(vertice_set,2):
            e_count += mat[i][j]
        if(e_count == ks_edge):
            ks_count += 1
            com_vertice_list[0].append(vertice_set)
            print('Find k{0} in G and {1}'.format(s,vertice_set))

    # Find kt in G_bar
    print('begin seek the k{0} in G_bar'.format(t))
    for vertice_set in itertools.combinations(range(n),t):
        e_count = 0
        for i,j in itertools.combinations(vertice_set,2):
            e_count += mat[i][j]
        if(e_count == 0):
            kt_count += 1
            com_vertice_list[1].append(vertice_set)
            print('Find k{0} in G_bar and {1}'.format(t,vertice_set))

    print("\nks of number : {0}, kt of number : {1}".format(ks_count,kt_count))

    return [ks_count,kt_count] #com_vertice_list

def r_count2(s,t,data):
    # find k_s in data
    mat = mat_data(data)
    n = len(mat)

    ks_count = 0
    kt_count = 0
    ks_edge  = sc.comb(s,2, exact=True)
#    kt_edge  = sc.comb(t,2, exact=True)

    com_vertice_list = [[ ], [ ]]

    # Find ks in G
    #print('begin seek the k{0} in G'.format(s))
    for vertice_set in itertools.combinations(range(n),s):
        e_count = 0
        for i,j in itertools.combinations(vertice_set,2):
            e_count += mat[i][j]
        if(e_count == ks_edge):
            ks_count += 1
            com_vertice_list[0].append(vertice_set)
            #print('Find k{0} in G and {1}'.format(s,vertice_set))

    # Find kt in G_bar
    #print('begin seek the k{0} in G_bar'.format(t))
    for vertice_set in itertools.combinations(range(n),t):
        e_count = 0
        for i,j in itertools.combinations(vertice_set,2):
            e_count += mat[i][j]
        if(e_count == 0):
            kt_count += 1
            com_vertice_list[1].append(vertice_set)
            #print('Find k{0} in G_bar and {1}'.format(t,vertice_set))

    #print("\nks of number : {0}, kt of number : {1}".format(ks_count,kt_count))

    return [ks_count,kt_count] #com_vertice_list

def W_count(s,t,data):
    # find k_s in data
    mat = mat_data(data)
    n = len(mat)

    ks_count = 0
    kt_count = 0
    ks_edge  = sc.comb(s,2, exact=True)
#    kt_edge  = sc.comb(t,2, exact=True)

    com_vertice_list = [[ ], [ ]]

    # Find ks in G
    #print('begin seek the k{0} in G'.format(s))
    for vertice_set in itertools.combinations(range(n),s):
        e_count = 0
        for i,j in itertools.combinations(vertice_set,2):
            e_count += mat[i][j]
        if(e_count == ks_edge):
            ks_count += 1
            com_vertice_list[0].append(vertice_set)
           # print('Find k{0} in G and {1}'.format(s,vertice_set))

    # Find kt in G_bar
   # print('begin seek the k{0} in G_bar'.format(t))
    for vertice_set in itertools.combinations(range(n),t):
        e_count = 0
        for i,j in itertools.combinations(vertice_set,2):
            e_count += mat[i][j]
        if(e_count == 0):
            kt_count += 1
            com_vertice_list[1].append(vertice_set)
           # print('Find k{0} in G_bar and {1}'.format(t,vertice_set))

   # print("\nks of number : {0}, kt of number : {1}".format(ks_count,kt_count))

    L = []
    for com_vertice in com_vertice_list:
        if len(com_vertice) > 0:
            for vertice_set in com_vertice:
                for i in range(3):
                    L.append(vertice_set[i])
    LL = []
    for i in range(8):
        LL.append(L.count(i))
    return LL #com_vertice_list



def get_mlist(n):
    if n >=8:
        print('sorry, your memory will be full')
        raise MemoryError
    
    mlist      = [['0']]
    temp_mlist = mlist.copy()

    for i in range(1,n-1):
        mlist = temp_mlist.copy()
        temp_mlist = []
        
        for j in itertools.product('01', repeat=i):
            row_part = j+ ('0',)
            for m in mlist:
                row_str = '' # stack the row_part
                temp_mlist.append([])
                for com,r in zip(m,row_part[:-1]):
                    row_str += r
                    temp_mlist[-1].append(com+r)
                temp_mlist[-1].append(row_str+row_part[-1])
            print('complete {0} part'.format(row_str+row_part[-1]))

    mlist = temp_mlist.copy()
    temp_mlist = []

    for j in itertools.product('01', repeat=i+1):
        if j[0] == '1':
            break # we get half
        row_part = j + ('0',)
        for m in mlist:
            row_str = ''
            temp_mlist.append([])
            for com,r in zip(m,row_part[:-1]):
                row_str += r
                temp_mlist[-1].append(com+r)
            temp_mlist[-1].append(row_str+row_part[-1])
        print('complete {0} part'.format(row_str+row_part[-1]))

    return temp_mlist
                
    










filename = '/test/test.txt'
type1 = '/test/test_json_list.txt'
type2 = '/test/test_json_str.txt'
type3 = '/test/test_str.txt'
result = 'D:/Python/order8_addition8.txt'
order8 = 'D:/Python/order8_graph.txt'
print("Here, some examples\n")

print("example 1:")
print("""test.txt ;  011
            101
            110""")
print("mat_data('{0}')".format(filename))
print("[[0,1,1],[1,0,1],[1,1,0]]")
print("---------------------------------------------------------------------")

print("example 2:")
data = """0111
1011
1101
1110
"""

print("""data = \"\"\"0111
1011
1101
1110\"\"\"
""")

print("print(data)")
print(data)
print("mat_data(data)")
print(mat_data(data))
print("---------------------------------------------------------------------")

L = [] # index list with k3 + k3_bar = 8
with open(result) as output:
    for idx, line in enumerate(output):
        temp = int(float(line))
        if temp == 8:
            L.append(idx)

size = 338

LL = []
with open(order8) as f:
    for idx,i in enumerate(L):
        c = f.seek(i*size)
        a = f.readline()
        a = json.loads(a)
        b = W_count(3,3,a)
        if idx % 100000 == 1:
            print('persent : {0}, idx : {1}'.format(idx/len(L),idx))
        if 4 not in b:
            LL.append(a)

L0 = []
L1 = []
L2 = []

for m in LL:
    WG = W_count(3,3,m)
    if 0 in WG:
        L0.append(m)
    elif 1 in WG:
        L1.append(m)
    elif 2 in WG:
        L2.append(m)
